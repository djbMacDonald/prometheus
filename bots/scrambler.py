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
    if  word_count> 1 and self._randomUtil.rollDice(self._frequency/word_count**2):
      random.shuffle(words)
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[self._target.lower()]]
      self._postUtil.addMessage(' '.join(words), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get))
      return
