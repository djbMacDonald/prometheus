import random
from model.identity import Identity
from constant.people import IDENTITIES
import urllib
import requests
import os
import string
from bots._bot import Bot
import re

class Third(Bot):
  
  _target = "Brenden"
  _frequency = .1
  
  @classmethod
  def description(cls):
    return "`Third` Makes {} talk in third person".format(cls._target)
  
  def contains_first(self):
    container = False
    if " i " in self._event.text().lower():
      container=True
    if "i " in self._event.text().lower():
      container=True
    if "i'm" in self._event.text().lower():
      container=True
    return container
  
  def run(self):
    if (
        self._event.isAMessage() 
        and self._event.isFrom(self._target) 
        and self._randomUtil.rollDice(self._frequency) 
        and self.contains_first()
        and not self._event.isFromABot()
    ):  
      text = self._event.text()
      text = re.sub(f'\\bi\\b', f' {self._target} ', text, flags = re.IGNORECASE)
      text = re.sub(f'\\bi\'m\\b', f' {self._target} is ', text, flags = re.IGNORECASE)
      
      self._postUtil.replacePost(self._event, text)