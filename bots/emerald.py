from constant.people import USERS
from model.identity import Identity
from bots._bot import Bot

class Emerald(Bot):
  
  _frequency = .1
  _target = 'Dakota'
  
  @classmethod
  def description(cls):
    return "`Emerald` Bugs {} about chaos emerald {}% of the time".format(cls._target, cls._frequency * 100)
    
  def run(self):
    if not self._event.isFrom(self._target) or self._event.isPartOfAThread() or self._event.isFromABot() or not not self._randomUtil.rollDice(self._frequency):
      return
    self._postUtil.addMessageToThread(':you-mean-the-chaos-emeralds:', self._event.channel(), self._event.id(), Identity(profilePicture = self._identityUtil.randomImageUrl()))
      