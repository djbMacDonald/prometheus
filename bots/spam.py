from bots._bot import Bot
import os
import requests
import random
import urllib

class Spam(Bot):
  
  _active = True
  _frequency = .01
  _numberOfEmotes = 23
  
  @classmethod
  def description(cls):
    return "`Spam` Has a {}% chance to post {} random reactions to a message".format(cls._frequency * 100, cls._numberOfEmotes)
  
  def run(self):
    if self._event.isFromABot() or not self._randomUtil.rollDice(self._frequency):
      return
    
    randomEmojis = random.sample(self._emoteUtil.getAll(), k=23)
    for emoji in randomEmojis:
      self._postUtil.addReactionToMessage(emoji)