from model.identity import Identity
from constant.people import IDENTITIES
from bots._bot import Bot

class Botify(Bot):
  
  _frequency = .2
  _target = "CJ"
  
  @classmethod
  def description(cls):
    return "`Botify` Has a {}% chance of replacing {}'s message with {}-bot's message".format(cls._frequency * 100, cls._target, cls._target)
  
  def run(self):
    if self._event.isAMessage() and self._event.isFrom(self._target) and self._randomUtil.rollDice(self._frequency) and not self._event.isFromABot():
      self._postUtil.replacePost(self._event, self._event.text())