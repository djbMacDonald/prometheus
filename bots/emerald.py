from model.identity import Identity
from bots._bot import Bot

class Emerald(Bot):
  
  _active = True
  
  _frequency = .05
  _target = 'Dakota'
  
  @classmethod
  def description(cls):
    return "Bugs {} about chaos emerald {}% of the time".format(cls._target, cls._frequency * 100)
    
  def run(self):
    if not self._event.isFrom(self._target) or self._event.isPartOfAThread() or self._event.isFromABot() or not self._randomUtil.rollDice(self._frequency):
      return
    self._addMessageToThread('Never forget: :you-mean-the-chaos-emeralds:', Identity(userName = 'Doctor Ivo "Eggman" Robotnik', emoji = 'robotnik'))
      