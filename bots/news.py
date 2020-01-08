import random
from model.identity import Identity
import urllib
import requests
import os
from bots._bot import Bot

class Mock(Bot):
  
  _target = "Ayshu"
  
  @classmethod
  def description(cls):
    return "`News`"
  
  def run(self):
    if self._event.isFromABot() or not self._event.isFrom(self._target):
      return;