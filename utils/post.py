from constant.settings import DEBUG
import os
import urllib
import requests
from model.post_data import PostData
from constant.channels import ALLOWED_CHANNELS
from constant.people import IDENTITIES
from model.identity import Identity

def poolCallback(args):
  # print('test', args)
  args.close()
  return

class Post:
  
  def __init__(self, pool, event):
    self._pool = pool
    self._event = event
  
  def _isAllowedToPostInThisChannel(self, channel):
    return channel in ALLOWED_CHANNELS
  
  def _sendRequest(self, postData):
    info = postData.get()
    if not self._isAllowedToPostInThisChannel(info['channel']):
      return;
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.parse.urlencode(info))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    
  def _addReaction(self, reaction, timestamp):
    if not self._isAllowedToPostInThisChannel(self._event.channel()):
      return;
    # move to post_data
    options = {
      'channel': self._event.channel(),
      'name': reaction, 
      'timestamp': timestamp,
      'as_user': False,
      'token': os.environ.get('DAKA')
    }
    url = 'https://www.slack.com/api/reactions.add?{}'.format(urllib.parse.urlencode(options))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    
  def _deleteMessage(self):
    if not self._isAllowedToPostInThisChannel(self._event.channel()):
      return;
    postData = {
       'channel': self._event.channel(),
       'ts': self._event.id(),
       'token': os.environ.get('SECRET')
    }
    url = 'https://www.slack.com/api/chat.delete?{}'.format(urllib.parse.urlencode(postData))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
  
  def addMessage(self, message, identity = None):
    if self._event.isPartOfAThread():
      self.addMessageToThread(message, identity)
    else:
      self.addMessageToChannel(message, identity)
  
  def addMessageToChannel(self, message, identity = None, channel = None):
    if not channel:
      channel = self._event.channel()
    postData = PostData(channel, message, identity)
    self._sendRequest(postData)
    
  def addMessageToThread(self, message, identity = None):
    postData = PostData(self._event.channel(), message, identity, threadId = self._event.id())
    self._sendRequest(postData)
    
  def useCommand(self, command, message, channel):
    postData = PostData(channel, message, identity, command = command)
    self._sendRequest(postData)
  
  def addReactionToMessage(self, reaction):
    self._addReaction(reaction, self._event.id());
    
  def addReactionToOriginalMessage(self, reaction):
    self._addReaction(reaction, self._event.threadId());
    
  def replacePost(self, message):
    identity = IDENTITIES[self._event.user()]
    self.addMessage(message, Identity(identity.get('username'), identity.get('profilePicture')))
    self._deleteMessage()
  
  def postEphemeral(self, data):
    url = 'https://www.slack.com/api/chat.postEphemeral?{}'.format(urllib.parse.urlencode(data))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    return   
    
    
  # def setChannelTopic(self, channel, message):
  #   if not self.isAllowedToPostInThisChannel(channel):
  #     return;
  #   postData = {
  #      'channel': channel,
  #      'topic': message,
  #      'token': os.environ.get('SECRET')
  #   }
  #   url = 'https://www.slack.com/api/conversations.setTopic?{}'.format(urllib.parse.urlencode(postData))
  #   print(url)
  #   self._pool.apply_async(requests.post, args=[url])