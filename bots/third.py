import random
from model.identity import Identity
import urllib
import requests
import os
import string
from bots._bot import Bot
import re

class Third(Bot):
  
  _active = True
  _target = "Brenden"
  _frequency = .1
  
  @classmethod
  def description(cls):
    return "Makes {} talk in third person".format(cls._target)
  
  def run(self):
    if (
        self._event.isAMessage() 
        and self._event.isFrom(self._target) 
        and self._randomUtil.rollDice(self._frequency) 
        and not self._event.isFromABot()
    ):  
      text = self._event.text()
      text = re.sub(f'\\bi\\b', f'{self._target}', text, flags = re.IGNORECASE)
      text = re.sub(f'\\bi\'m\\b', f'{self._target} is', text, flags = re.IGNORECASE)
      
      if text == self._event.text():
        return
      
      self._postUtil.replacePost(text)