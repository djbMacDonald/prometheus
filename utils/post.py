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
  
  def __init__(self, event, className, actionQueue):
    self._event = event
    self._caller = className
    self._queue = actionQueue
    
  def addReactionToMessage(self, reaction):
    self._queue.addReaction(self._caller, self._event.channel(), self._event.id(), reaction)
    
  def addReactionToOriginalMessage(self, reaction):
    self._queue.addReaction(self._caller, self._event.channel(), self._event.threadId(), reaction)
  
  def addMessageToChannel(self, message, identity = None, channel = None):
    if not channel:
      channel = self._event.channel()
    self._queue.addReply(self._caller, self._event.channel(), None, message, identity)
  
  def addMessage(self, message, identity = None):
    if self._event.isPartOfAThread():
      self._queue.addReply(self._caller, self._event.channel(), self._event.id(), message, identity)
    else:
      self.addMessageToChannel(message, identity)
    
  def useCommand(self, command, message, channel):
    self._queue.addCommand(self._caller, channel, command, message, identity)
    
  def replacePost(self, message):
    identity = IDENTITIES[self._event.user()]
    self._queue.addReplacement(self._caller, self._event.channel(), self._event.id(), self._event.threadId(), message, Identity(identity.get('username'), identity.get('profilePicture')))