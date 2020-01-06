from constant.settings import DEBUG
import os
import urllib
import requests
from model.post_data import PostData
from constant.channels import ALLOWED_CHANNELS

class Post:
  
  def __init__(self, pool):
    self._pool = pool
  
  def isAllowedToPostInThisChannel(self, channel):
    return channel in ALLOWED_CHANNELS
  
  def addMessage(self, message, channel, threadId, identity = None):
    if threadId:
      self.addMessageToThread(message, channel, threadId, identity)
    else:
      self.addMessageToChannel(message, channel, identity)
  
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
    info = postData.get()
    if not self.isAllowedToPostInThisChannel(info['channel']):
      return;
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.parse.urlencode(info))
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
    url = 'https://www.slack.com/api/reactions.add?{}'.format(urllib.parse.urlencode(options))
    self._pool.apply_async(requests.get, args=[url])
    
  def deleteMessage(self, channel, id):
    if not self.isAllowedToPostInThisChannel(channel):
      return;
    postData = {
       'channel': channel,
       'ts': id,
       'token': os.environ.get('SECRET')
    }
    url = 'https://www.slack.com/api/chat.delete?{}'.format(urllib.parse.urlencode(postData))
    self._pool.apply_async(requests.get, args=[url])

  def getAllEmojis(self):
    postData = {
      'token': os.environ.get('SECRET')
    }
    req = requests.get('https://slack.com/api/emoji.list?{}'.format(urllib.parse.urlencode(postData)))
    return list(req.json().get('emoji').keys())