from utils.post import Post
from utils.identity import Identity
from utils.random import Random
from utils.ban import Ban
from utils.channel import Channel
from utils.mongo import Mongo
from utils.trigger import Trigger
from utils.emote import Emote
from utils.server import hardDisableAllBots

class Bot(object):
  
  _active = False
  _frequency = 0
  
  def __init__(self, eventModel, pool, mongoClient, user, emotes, actionQueue):
    self._event = eventModel
    self._user = user
    self._postUtil = Post(eventModel, self.__class__.__name__, actionQueue)
    self._identityUtil = Identity()
    self._randomUtil = Random()
    self._banUtil = Ban()
    self._channelUtil = Channel()
    self._mongoUtil = Mongo(mongoClient)
    self._triggerUtil = Trigger(eventModel)
    self._emoteUtil = Emote(emotes)
    
  @classmethod
  def formatDescription(cls):
    description = cls.description()
    if description == "":
      return description
    if hardDisableAllBots or not cls._active:
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