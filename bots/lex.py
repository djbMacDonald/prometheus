import random
import re
from bots._bot import Bot

class Lex(Bot):
  
  _active = True
  _frequency = .01
  
  @classmethod
  def description(cls):
    return "Scrambles letters in some words."
  
  def run(self): 
    if (
        self._event.isFromABot() 
        or not self._event.text()
        or not self._event.isAMessage() 
        or not self._event.isFromChaosUser() 
        or not self._randomUtil.rollDice(self._frequency)
    ):
      return
    
    words = re.findall(r'\w+', self._event.text())
    longWord = max(words, key=len)
    scramble = self._scrambleWord(longWord)
    if longWord == scramble:
      return;
    
    newString = self._event.text().replace(longWord, scramble)
    self._replacePost(newString)
  
  def _scrambleWord(self, word):
    if len(word) < 4:
      return word
    if len(word) > 5:
      first, mid, last = word[:2], word[2:-2], word[-2:]
    else:
      first, mid, last = word[:1], word[1:-1], word[-1:]
    chars = list(mid)
    random.shuffle(chars)
    newMid = ''.join(chars)
    return first + newMid + last