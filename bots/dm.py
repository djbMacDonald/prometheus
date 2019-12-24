import random
from model.identity import Identity

from util.random import RandomUtil
from util.message import MessageUtil

from constants.dungeon import ABILITIES, SAVES, SPECIAL, ACTIONS, DANGERS
from constants.language import VOWELS

class DmBot:
  
  _frequency = 1/1
  _save = 1/5
  _special = 1/5
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._messageUtil = MessageUtil(pool)
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFromABot():
      return;
    if self._randomUtil.rollDice(self._frequency):
      message = 'Roll {} to {} the {}'.format(self._createRollMessage(), random.choice(ACTIONS), random.choice(DANGERS))
      identity = Identity(userName = 'Dungeon Master')
      if self._event.isPartOfAThread():
        self._messageUtil.addMessageToThread(message, self._event.channel(), self._event.id(), identity)
      else:
        self._messageUtil.addMessageToChannel(message, self._event.channel(), identity)
        
  def _createRollMessage(self):
    if self._randomUtil.rollDice(self._save):
      message = '{} saving throw'.format(random.choice(SAVES))
    else:
      message = '{} check'.format(random.choice(ABILITIES))
    if self._randomUtil.rollDice(self._special):
      message += ' ' + random.choice(SPECIAL)
    if message.startswith(VOWELS):
      message = 'an {}'.format(message)
    else: 
      message = 'a {}'.format(message)
    return message
