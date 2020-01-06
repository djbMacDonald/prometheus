import random
from bots._bot import Bot

class Nice(Bot):
  
  _min = 3
  _max = 10
  
  @classmethod
  def description(cls):
    return "`Nice` If you say nice, will respond with 'nice', {} to {} times".format(cls._min, cls._max)
  
  def run(self):
    if self._event.isFromABot() or not self._event.text() or len(self._event.text()) < 1:
      return;
    if self._event.text() == 'nice' and not self._event.isPartOfAThread():
      nices = 0
      while nices < self._min or (self._randomUtil.rollDice(8.0/10) and nices < self._max):
        self._postUtil.addMessageToThread('nice', self._event.channel(), self._event.id(), self._identityUtil.getRandomIdentity())
        nices = nices+1
