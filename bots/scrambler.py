import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity

class Scrambler(Bot):

  _active = True
  _frequency = 4
  _target = 'Drew' 
  _minWords = 4
  
  @classmethod
  def description(cls):
    return "Has a {}%/(word count^2) chance to scramble {}'s message. Ony words if message has {} or more words".format(cls._frequency * 100, cls._target, cls._minWords)
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target):
      return
    words = self._event.text().split(' ')
    word_count=len(words)
    if word_count >= self._minWords and self._randomUtil.rollDice(self._frequency / word_count ** 2):
      random.shuffle(words)
      self._postUtil.replacePost(' '.join(words))
      return
