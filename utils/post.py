from constant.settings import DEBUG
import os
import urllib
import requests
from model.post_data import PostData
from constant.channels import allowed_channel_ids
from constant.people import IDENTITIES
from model.identity import Identity
from utils.log import Log

def poolCallback(args):
  # print('test', args)
  args.close()
  return

class Post:
  
  def __init__(self, pool, event, className, actionQueue):
    self._log = Log()
    self._pool = pool
    self._event = event
    self._caller = className
    self._queue = actionQueue
    
  def _truncate(self, message):
    return message[:20] + (message[20:] and '...')
  
  def _isAllowedToPostInThisChannel(self, channel):
    return channel in allowed_channel_ids()
  
  def _sendRequest(self, postData):
    info = postData.get()
    if not self._isAllowedToPostInThisChannel(info['channel']):
      return;
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.pa
    
  def _addReaction(self, reaction, timestamp):
    if not self._isAllowedToPostInThisChannel(self._event.channel()):
      return;
    self._queue.addReaction(self._caller, self._event.channel(), timestamp, reaction)
    
  def addReactionToMessage(self, reaction):
    self._addReaction(reaction, self._event.id());
    
  def addReactionToOriginalMessage(self, reaction):
    self._addReaction(reaction, self._event.threadId());
  
  def addMessageToChannel(self, message, identity = None, channel = None):
    if not channel:
      channel = self._event.channel()
    if not self._isAllowedToPostInThisChannel(channel):
      return;
    self._queue.addReply(self._caller, self._event.channel(), None, message, identity)
    
  def addMessageToThread(self, message, identity = None):
    if not self._isAllowedToPostInThisChannel(self._event.channel()):
      return;
    self._queue.addReply(self._caller, self._event.channel(), self._event.id(), message, identity)
  
  def addMessage(self, message, identity = None):
    if self._event.isPartOfAThread():
      self.addMessageToThread(message, identity)
    else:
      self.addMessageToChannel(message, identity)
    
  def useCommand(self, command, message, channel):
    if not self._isAllowedToPostInThisChannel(self._event.channel()):
      return;
    self._queue.addCommand(self._caller, channel, command, message, identity)
    
  def replacePost(self, message):
    if not self._isAllowedToPostInThisChannel(self._event.channel()):
      return;
    identity = IDENTITIES[self._event.user()]
    self._queue.addReplacement(self._caller, self._event.channel(), self._event.id(), self._event.threadId(), message, Identity(identity.get('username'), identity.get('profilePicture')))
  
  def postEphemeral(self, data):
    url = 'https://www.slack.com/api/chat.postEphemeral?{}'.format(urllib.parse.urlencode(data))
    self._log.logEvent("{}: {}-bot makes an ephemeral post".format(self._event.channelName(), self._caller))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    return   