from utils.post import PostUtil
import random
from model.identity import Identity
import urllib
import requests
import os
from constant.people import USERS
from utils.identity import IdentityUtil 

class ThreadHereBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
  
  def run(self):
    lines = open('threads.txt', 'r').read().splitlines()
    if self._event.threadId() in lines:
      return
    
    if self._event.text() and self._event.text().lower() == "silence chaos seed":
      self._recordThread()
      self._postUtil.addReaction("salute_cap", self._event.channel(), self._event.id())
      self._postUtil.addReaction("squirrel", self._event.channel(), self._event.threadId())
      return
    # if self._event.isFromABot() or not self._event.threadId() or not self._event.isInChannel('Chaos'):
    if self._event.isFromABot() or not self._event.threadId() or not self._event.isInChannel('Megamoji'):
      return;
    
    lines = open('threads.txt', 'r').read().splitlines()
    if str(self._event.threadId()) in lines:
      return

    messages = self._checkForReplies()
    targetNumber = random.randint(3, 10)
    if not messages or not messages[0] or not messages[0]['reply_count'] or messages[0]['reply_count'] < targetNumber:
      return
    userMap = map(self._identityUtil.pingUser, USERS.values())
    notification = "Hey {}! There's a thread here!".format(" ".join(userMap))
    # self._postUtil.addMessageToThread(notification, self._event.channel(), self._event.threadId())
    
  def _recordThread(self):
    f = open('threads.txt', 'a')
    f.write("{}\n".format(self._event.threadId()))
    f.close()
    # lines = open('threads.txt', 'r').read().splitlines()
      
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
    return req.json().get('messages')