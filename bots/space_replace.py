import random
from model.identity import Identity
from constant.people import USERS
from bots._bot import Bot

class SpaceReplace(Bot):
  
  _active = True
  _frequency = .01
  _target = 'Brenden'
  
  @classmethod
  def description(cls):
    return "Has a {}% chance to replace {}'s spaces with dashes".format(cls._frequency * 100, cls._target)
  
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target) or not self._randomUtil.rollDice(self._frequency):
      return
    if ' ' in self._event.text():
      message = self._event.text().replace(' ', '-')
      self._postUtil.replacePost(message)
      return
