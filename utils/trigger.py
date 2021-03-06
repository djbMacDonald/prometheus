from utils.identity import Identity
from utils.random import Random
from utils.ban import Ban
from utils.channel import Channel
from utils.mongo import Mongo

class Trigger:
  
  def __init__(self, event):
    self._randomUtil = Random()
    self._event = event
  
  def targetSendsMessageAnywhere(self, target, chance = 1):
    return (
      self._event.isFrom(target) 
      and not self._event.isFromABot() 
      and self._event.isAMessage()
      and self._randomUtil.rollDice(chance)
    )
  
  def targetSendsMessageToChannel(self, target, chance = 1):
    return (
      self.targetSendsMessageAnywhere(target, chance) 
      and not self._event.isPartOfAThread()
    )
    
  def chaosUserSendsMessage(self, event):
    return (
      event.isFromChaosUser()
      and event.text() is not None
      and not event.isFromABot()
    )
  
  def messageMatchesText(self, message, matchText, ignoreCase):
    if ignoreCase:
      return message and message.lower() == matchText.lower()
    return message and message == matchText
    