import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot

class Crab(Bot):
  
  _active = False
  _frequency = 0
  _target = 'Ayshu'
  
  @classmethod
  def description(cls):
    return "`Crab` Has a {}% chance to call {} a crab".format(cls._frequency * 100, cls._target)
  
  def run(self):
    if self._event.isFromABot() or not self._event.isFrom(self._target) or not self._randomUtil.rollDice(self._frequency):
      return;
    self._postUtil.addReactionToMessage("crab")