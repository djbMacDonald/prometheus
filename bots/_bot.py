from utils.identity import Identity as IdentityUtil
from utils.random import Random
from utils.ban import Ban
from utils.channel import Channel
from utils.mongo import Mongo
from utils.trigger import Trigger
from utils.emote import Emote
from constant.people import IDENTITIES
from model.identity import Identity

class Bot(object):
  
  _active = False
  _frequency = 1
  
  def __init__(self, eventModel, mongoClient, user, emotes, actionQueue):
    self._event = eventModel
    self._user = user
    self._identityUtil = IdentityUtil()
    self._randomUtil = Random()
    self._banUtil = Ban()
    self._channelUtil = Channel()
    self._mongoUtil = Mongo(mongoClient)
    self._triggerUtil = Trigger(eventModel)
    self._emoteUtil = Emote(emotes)
    self._queue = actionQueue
    
  @classmethod
  def formatDescription(cls):
    description = cls.description()
    if description == "":
      return description
    if not cls._active:
      return "DISABLED: " + description
    return description
  
  @classmethod
  def description(cls):
    return ""
  
  def safeRun(self):
    if not self._active:
      return
    self.run()
  
  def run(self):
    return
  
  def getListView(self):
    return
  
  def _addReactionToMessage(self, reaction, priority = 1):
    self._queue.addReaction(self.__class__.__name__, self._event.channel(), self._event.id(), reaction, priority)
    
  def _addReactionToOriginalMessage(self, reaction):
    self._queue.addReaction(self.__class__.__name__, self._event.channel(), self._event.threadId(), reaction)
  
  def _addMessageToThread(self, message, identity = None):
    self._queue.addReply(self.__class__.__name__, self._event.channel(), self._event.id(), message, identity)
    
  def _addMessage(self, message, identity = None):
    if self._event.isPartOfAThread():
      self._queue.addReply(self.__class__.__name__, self._event.channel(), self._event.id(), message, identity)
    else:
      self._addMessageToChannel(message, identity)
      
  def _addMessageToChannel(self, message, identity = None, channel = None):
    if not channel:
      channel = self._event.channel()
    self._queue.addReply(self.__class__.__name__, channel, None, message, identity)
    
  def _useCommand(self, command, message, channel):
    self._queue.addCommand(self.__class__.__name__, channel, command, message, identity)
    
  def _replacePost(self, message):
    identity = IDENTITIES.get(self._event.user())
    if identity:
      self._queue.addReplacement(self.__class__.__name__, self._event.channel(), self._event.id(), self._event.threadId(), message, Identity(identity.get('username'), identity.get('profilePicture')), attachments = self._event.attachments())
    else:
      self._queue.addReplacement(self.__class__.__name__, self._event.channel(), self._event.id(), self._event.threadId(), message, attachments = self._event.attachments())
    
  def _targetSendsMessageToChannel(self):
    return self._triggerUtil.targetSendsMessageToChannel(self._target, self._frequency)
  
  def _targetSendsMessageAnywhere(self):
    return self._triggerUtil.targetSendsMessageAnywhere(self._target, self._frequency)
  
  def _chaosUserSendsMessage(self):
    return self._triggerUtil.chaosUserSendsMessage(self._event)
  
  def _messageMatchesText(self, matchText, ignoreCase = True):
    return self._triggerUtil.messageMatchesText(self._event.text(), matchText, ignoreCase)