import random
from bots._bot import Bot

class Lex(Bot):
  
  _active = False
  _frequency = .01
  
  @classmethod
  def description(cls):
    return "Scrambles letters in some words."
  
  def run(self):
    if (
        self._event.isFromABot() 
        or not not self._event.text()
        or not self._event.isAMessage() 
        or not self._event.isFromChaosUser() 
        or not self._randomUtil.rollDice(self._frequency)
    ):
      return

    newMessage = self._event.text()
    words = newMessage.split(' ');
    
    thing = map(self._doStuff, words)
  
  def doStuff(self, word):
    if len(word) < 5:
      return word
    return word