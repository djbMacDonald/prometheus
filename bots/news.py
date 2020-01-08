import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot
from xml.dom import minidom

class News(Bot):
  
  _target = "Ayshu"
  _frequency = .01
  _url = "https://www.buzzfeed.com/lol.xml"
  
  @classmethod
  def description(cls):
    return "`News`"
  
  def run(self):
    if self._event.isFromABot() or not self._event.isInChannel('Megamoji') or not self._event.:
      return
    # if self._event.isFromABot() or not self._event.isFrom(self._target) or not self._randomUtil.rollDice(self._frequency):
    #   return;
    
    req = requests.get(self._url)
    mydoc = minidom.parseString(req.content)
    items = mydoc.getElementsByTagName('item')  
    # self._postUtil.addMessageToThread(random.choice(items).getElementsByTagName("title")[0].firstChild.nodeValue, self._event.channel(), self._event.id())
    