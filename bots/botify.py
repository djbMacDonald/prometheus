from model.identity import Identity
from bots._bot import Bot

class Botify(Bot):
  
  _active = True
  
  _frequency = .2
  _target = "CJ"
  
  @classmethod
  def description(cls):
    return "Has a {}% chance of replacing {}'s message with {}-bot's message".format(cls._frequency * 100, cls._target, cls._target)
  
  def run(self):
    if self._triggerUtil.targetSendsMessageAnywhere():
      self._replacePost(self._event.text())