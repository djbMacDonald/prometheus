import os
import urllib
import requests

from model.post_data import PostData

from constant.channels import ALLOWED_CHANNELS
from constant.settings import DEBUG

class PostUtil:
  
  def __init__(self, pool):
    self._pool = pool
  
  def isAllowedToPostInThisChannel(self, channel):
    return channel in ALLOWED_CHANNELS
  
  def addMessage(self, message, channel, threadId, identity = None):
    if threadId:
      addMessageToThread(message, channel, threadId, identity)
    else:
      addMessageToChannel(message, channel, identity)
  
  def addMessageToChannel(self, message, channel, identity = None):
    postData = PostData(channel, message, identity)
    self._sendRequest(postData)
    
  def addMessageToThread(self, message, channel, threadId, identity = None):
    postData = PostData(channel, message, identity, threadId = threadId)
    self._sendRequest(postData)
    
  def useCommand(self, command, message, channel):
    postData = PostData(channel, message, identity, command = command)
    self._sendRequest(postData)
    
  def _sendRequest(self, postData):
    if not self.isAllowedToPostInThisChannel(channel):
      return;
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.urlencode(postData.get()))
    if DEBUG:
      print(url)
    self._pool.apply_async(requests.get, args=[url])
    
  def addReaction(self, reaction, channel, timestamp):
    if not self.isAllowedToPostInThisChannel(channel):
      return;
    # move to post_data
    options = {
      'channel': channel,
      'name': reaction, 
      'timestamp': timestamp,
      'as_user': False,
      'token': os.environ.get('DAKA')
    }
    url = 'https://www.slack.com/api/reactions.add?{}'.format(urllib.urlencode(options))
    self._pool.apply_async(requests.get, args=[url])
    
  def deleteMessage(self, channel, id):
    if not self.isAllowedToPostInThisChannel(channel):
      return;
    postData = {
       'channel': self.channel(),
       'ts': self.id(),
       'token': os.environ.get('SECRET')
    }
    url = 'https://www.slack.com/api/chat.delete?{}'.format(urllib.urlencode(postData))
    self._pool.apply_async(requests.get, args=[url])
