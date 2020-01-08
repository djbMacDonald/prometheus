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
    # if self._event.isFromABot() or not self._event.isFrom(self._target):
    #   return;
    
    req = resp = requests.get(self._url)
    mydoc = minidom.parse(req.content)