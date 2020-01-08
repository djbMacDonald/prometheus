import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity

class Scrambler:

  _frequency = .01
  _target = 'Drew' 
  
  @classmethod
  def description(cls):
    return "`Scrambler` Has a {}% chance to scramble {}'s message".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target):
      return
    words = self._event.text().split(' ')
    if len(words) > 1 and self._randomUtil.rollDice(self._frequency):
      random.shuffle(words)
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[self._target.lower()]]
      self._postUtil.addMessage(' '.join(words), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get))
      return
