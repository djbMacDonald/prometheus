from utils.post import Post
from utils.identity import Identity
from utils.random import Random
from utils.ban import Ban
from utils.channel import Channel
from utils.mongo import Mongo
from utils.trigger import Trigger
from utils.emote import Emote

class Bot(object):
  
  _active = False
  
  def __init__(self, eventModel, pool, mongoClient, user, emotes):
    self._event = eventModel
    self._user = user
    self._postUtil = Post(pool, eventModel)
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