from utils.post import PostUtil
import random
from model.identity import Identity
import urllib
import requests
import os

class MockBot:
  
  @classmethod
  def description(cls):
    return "`Mock bot` If you use the spongebob-mock emote on a message,  it will post to a thread that weird alternating caps thing version of the message."
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
  
  def run(self):
    if self._event.isFromABot():
      return;
    
    # this needs to be moved to util
    postData = {
      'token': os.environ.get('SECRET'),
      'channel': self._event.channel(),
      'latest': self._event.id(),
      'inclusive': True,
      'oldest': self._event.id()
    }
    req = requests.get('https://slack.com/api/channels.history?{}'.format(urllib.parse.urlencode(postData)))
    
    message = req.json().get('messages')
    if not message or len(message) < 1:
      return
    message = message[0]
    if message.get('replies') or message.get('thread_ts'):
      return
    if not message.get('reactions'):
      return
    for reaction in message.get('reactions'):
      if reaction.get('name') != 'spongebob-mock' or reaction.get('count') < 1:
        return
    self.text = message.get('text')
    message = self._mockString(self.text)
    self._postUtil.addMessageToThread(message, self._event.channel(), self._event.id(), Identity('sPoNgeBoB', 'https://emoji.slack-edge.com/TDBEDSEQZ/spongebob-mock/3b66c2fdf2b77a8d.png'))
    return 'end'
    
  def _mockString(self, str):
    ret = ""
    i = True  # capitalize
    for char in str:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret
