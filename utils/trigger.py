from utils.post import Post
from utils.identity import Identity
from utils.random import Random
from utils.ban import Ban
from utils.channel import Channel
from utils.mongo import Mongo

class Trigger:
  
  def __init__(self):
    self._randomUtil = Random()
  
  def targetSendsMessageToChannel(self, event, target, chance = 1):
    return (
      not event.isFrom(target) 
      or event.isPartOfAThread() 
      or event.isFromABot() 
      or not event.isAMessage()
      or not 
      return
    if not self._randomUtil.rollDice(self._frequency):
      return
  
  def targetSendsMessageAnywhere(self, event, target, chance = 1):
    return (
      not self._event.isFrom(self._target) 
      or self._event.isPartOfAThread() 
      or self._event.isFromABot():
      or not self._randomUtil.rollDice(self._frequency
    )