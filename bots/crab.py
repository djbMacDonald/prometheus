import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot

class Crab(Bot):
  
  _frequency = .05
  _target = 'Ayshu'
  
  @classmethod
  def description(cls):
    return "`Crab` Has a {}% chance to call Aysh a crab".format(cls._freqwuency * 100)
  
  def run(self):
    if self._event.isFromABot() or not self._event.isFrom(self._target):
      return;
    self._postUtil.addReaction("salute_cap", self._event.channel(), self._event.id())