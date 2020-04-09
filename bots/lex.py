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
    
    words = map(self._doStuff, self._event.text().split(' '))
    newMessage = 
    if self._event.text() == newMessage:
      return;
    self._postUtil.replacePost(newMessage)
  
  def doStuff(self, word):
    if len(word) < 4:
      return word
    first, mid, last = word[0], word[1:-1], word[-1]
    return first + shuffle_string(mids) + last