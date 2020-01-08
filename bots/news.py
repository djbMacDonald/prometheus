import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot
from xml.dom import minidom

class News(Bot):
  
  _target = "Ayshu"
  _url = "https://www.buzzfeed.com/lol.xml"
  
  @classmethod
  def description(cls):
    return "`News`"
  
  def run(self):
    if not self._event.isInChannel('Megamoji'):
      return
    # if self._event.isFromABot() or not self._event.isFrom(self._target):
    #   return;
    
    req = resp = requests.get(self._url)
    # print(req.content)
    mydoc = minidom.parseString(req.content)
    items = mydoc.getElementsByTagName('item')
    print(items[0].attributes['title'].value)
    # self._postUtil.addMessageToThread(items[0].title, self._event.channel(), self._event.threadId())
    