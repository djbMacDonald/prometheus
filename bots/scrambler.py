import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity

class Scrambler(Bot):

  _frequency = 5
  _target = 'Drew' 
  
  @classmethod
  def description(cls):
    return "`Scrambler` Has a {}%/(word count^2) chance to scramble {}'s message".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target):
      return
    words = self._event.text().split(' ')
    word_count=len(words)
    if  word_count> 3 and self._randomUtil.rollDice(self._frequency/word_count**2):
      random.shuffle(words)
      self._postUtil.replacePost(' '.join(words))
      return
