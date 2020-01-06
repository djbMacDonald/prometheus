from utils.post import PostUtil
from utils.identity import IdentityUtil
import random
from utils.random import RandomUtil

class NiceBot():
  
  @classmethod
  def description(cls):
    return "`Name bot` ".format()
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
    self._randomUtil = RandomUtil()
  
  def run(self):
    if self._event.isFromABot() or not self._event.text() or len(self._event.text()) < 1:
      return;
    if self._event.text() == 'nice' and not self._event.isPartOfAThread():
      nices = 0
      while nices < 3 or (self._randomUtil.rollDice(8.0/10) and nices < 10):
        self._postUtil.addMessageToThread('nice', self._event.channel(), self._event.id(), self._identityUtil.getRandomIdentity())
        nices = nices+1
