from bots._bot import Bot
import os
import requests
import random
import urllib

class Spam(Bot):
  
  _active = True
  _frequency = .005
  _minNumberOfEmotes = 10
  _maxNumberOfEmotes = 23
  
  @classmethod
  def description(cls):
    return "Has a {}% chance to post {}-{} random reactions to a message".format(cls._frequency * 100, cls._minNumberOfEmotes, cls._maxNumberOfEmotes)
  
  def run(self):
    if self._event.isFromABot() or not self._randomUtil.rollDice(self._frequency):
      return
    randomEmojis = random.sample(self._emoteUtil.getAll(), k=self._randomUtil.randRange(self._minNumberOfEmotes, self._maxNumberOfEmotes))
    for emoji in randomEmojis:
      self._addReactionToMessage(emoji, 0)