from bots.bot import Bot
import os
import requests
import random
import urllib

class Spam(Bot):
  
  _frequency = .01
  _numberOfEmotes = 23
  
  @classmethod
  def description(cls):
    return "`Spam` Has a {}% chance to post {} random reactions to a message".format(cls._frequency * 100, cls._numberOfEmotes)
  
  def run(self):
    if not self._randomUtil.rollDice(self._frequency):
      return
    
    emojis = self._postUtil.getAllEmojis()
    
    for i in range(1, self._numberOfEmotes):
      self._postUtil.addReaction(random.choice(emojis), self._event.channel(), self._event.id())