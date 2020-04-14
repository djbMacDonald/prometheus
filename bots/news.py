import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot
from xml.dom import minidom

class News(Bot):
  
  _active = True
  _target = "Ayshu"
  _frequency = .005
  _url = "https://www.buzzfeed.com/lol.xml"
  
  @classmethod
  def description(cls):
    return "Posts a Buzzfeed headline for {} {}% of the time.".format(cls._target, cls._frequency * 100)
  
  def run(self):
    if self._event.isFromABot() or not self._event.isFrom(self._target) or not self._randomUtil.rollDice(self._frequency) or self._event.isPartOfAThread():
      return;
    req = requests.get(self._url)
    mydoc = minidom.parseString(req.content)
    items = mydoc.getElementsByTagName('item')  
    self._addMessageToThread(random.choice(items).getElementsByTagName("title")[0].firstChild.nodeValue)
    