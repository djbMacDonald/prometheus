import random
from model.identity import Identity
from constant.people import USERS
from bots._bot import Bot

class Greek(Bot):
  
  _active = False
  _frequency = .01
  _target = 'Brenden'
  
  _stuff = {
    'a',
    'b',
    'g'
    'd'
    ezh'
  }
  
  @classmethod
  def description(cls):
    return ""
    # return "Has a {}% chance to replace {}'s spaces with dashes".format(cls._frequency * 100, cls._target)
  
  def run(self):
    if not self._chaosUserSendsMessage() or not not self._randomUtil.rollDice(self._frequency):
      return
    # if ' ' in self._event.text():
    #   message = self._event.text().replace(' ', '-')
    #   self._replacePost(message)
    #   return
