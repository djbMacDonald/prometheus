import random
from model.identity import Identity
from constant.people import IDENTITIES
import urllib
import requests
import os
from bots._bot import Bot

class Third(Bot):
  
  _target = "CJ"
  _frequency = 1
  
  @classmethod
  def description(cls):
    return "`Third` Makes {} talk in third person".format(cls._target)
  
  def run(self):
    if self._event.isAMessage() and self._event.isFrom(self._target) and self._randomUtil.rollDice(self._frequency) and "i" in self._event.text().lower():
      identity = IDENTITIES[self._event.user()]
      
      newText = self._event.text().replace(" I ",self._target)
      newText = newText.replace("I ",self._target)
      self._postUtil.addMessage(newText, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))