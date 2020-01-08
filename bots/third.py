import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot
from xml.dom import minidom

class Third(Bot):
  
  _target = "CJ"
  _frequency = 1
  _url = "https://www.buzzfeed.com/lol.xml"
  
  @classmethod
  def description(cls):
    return "`News`"
  
  def run(self):
    if self._event.isAMessage() and self._event.isFrom(self._target) and self._randomUtil.rollDice(self._frequency) and [" I ","I "] in self._event.text().lower():
      self._event.text().replace(" I ",self._target)
      self._event.text().replace("I ",self._target)
      self._postUtil.addMessage(self._event.text(), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))