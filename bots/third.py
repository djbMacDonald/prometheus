import random
from model.identity import Identity
from constant.people import IDENTITIES
import urllib
import requests
import os
import string
from bots._bot import Bot

class Third(Bot):
  
  _target = "Brenden"
  _frequency = .1
  _post_text =""
  
  @classmethod
  def description(cls):
    return "`Third` Makes {} talk in third person".format(cls._target)
  def contains_first(self):
    container=False
    if " i " in self._event.text().lower():
      container=True
    if "i " in self._event.text().lower():
      container=True
    if "i'm" in self._event.text().lower():
      container=True
    return container
  
  def run(self):
    if self._event.isAMessage() and self._event.isFrom(self._target) and self._randomUtil.rollDice(self._frequency) and self.contains_first():
      identity = IDENTITIES[self._event.user()]
      self._post_text=self._event.text()
      self._post_text = self._post_text.lower().replace(" i "," "+(self._target)+" ")
      self._post_text = self._post_text.lower().replace("i ",(self._target)+" ")
      self._post_text = self._post_text.lower().replace("i'm",(self._target)+" is")
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      self._postUtil.addMessage(self._post_text, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))