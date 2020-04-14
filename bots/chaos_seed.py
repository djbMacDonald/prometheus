import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot

class ChaosSeed(Bot):
  
  _active = True
  _fileName = 'threads.txt'
  _minCount = 6
  _maxCount = 10
  
  @classmethod
  def description(cls):
    return "If somewhere between {} and {} posts are made in a thread, pings all Chaos users not currently in thread".format(cls._minCount, cls._maxCount)
  
  def run(self):
    lines = open(self._fileName, 'r').read().splitlines()
    if self._event.threadId() in lines:
      return
    
    if self._event.text() and self._event.text().lower() == "silence chaos seed":
      self._recordThread()
      self._addReactionToMessage("salute_cap")
      self._addReactionToOriginalMessage("squirrel")
      return
    if self._event.isFromABot() or not self._event.threadId():
      return;
    
    lines = open(self._fileName, 'r').read().splitlines()
    if str(self._event.threadId()) in lines:
      return

    messages = self._checkForReplies()
    targetNumber = random.randint(self._minCount, self._maxCount)
    if not messages or not messages[0] or not messages[0]['reply_count'] or messages[0]['reply_count'] < targetNumber:
      return
    threadUsers = map(lambda x: x.get('id'), self._user._db.users.find({'threads': True}))
    users = self._filterUsers(threadUsers, messages[0]['reply_users'])
    userMap = map(self._identityUtil.pingUser, users)
    notification = "Hey {}! There's a thread here!".format(" ".join(userMap))
    self._addMessageToThread(notification, Identity('Chaos Seed', None, 'chaos'))
    self._recordThread()
    
  def _recordThread(self):
    f = open(self._fileName, 'a')
    f.write("{}\n".format(self._event.threadId()))
    f.close()
      
#   move to utils
  def _checkForReplies(self):
    postData = {
      'token': os.environ.get('SECRET'),
      'channel': self._event.channel(),
      'thread_ts': self._event.threadId(),
      'channel': self._event.channel(),
      'latest': self._event.id(),
      'inclusive': True,
      'oldest': self._event.id()
    }
    req = requests.get('https://slack.com/api/channels.replies?{}'.format(urllib.parse.urlencode(postData)))
    
    response = req.json()    
    return response.get('messages')
  
  # move to util
  def _filterUsers(self, fullList, subtractList):
    return list(set(fullList) - set(subtractList))