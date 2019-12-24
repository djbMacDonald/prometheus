import random
from identity import Identity

from util.random import RandomUtil
from util.message import MessageUtil

class DmBot:
  
  _frequency = 
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._messageUtil = MessageUtil(pool)
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFromABot():
      return;
    if self._randomUtil.rollDice(event_constants.CHANCE_FOR_DM):
      message = 'Roll {} to {} the {}'.format(self._createRollMessage(), random.choice(event_constants.ACTIONS), random.choice(event_constants.DANGERS))
      identity = Identity(userName = 'Dungeon Master')
      if self._event. isPartOfAThread():
        self._postUtil.addMessageToThread(message, self._event.channel(), self._event.id(), identity)
      else:
        self._postUtil.addMessageToChannel(message, self._event.channel(), identity)
        
  def _createRollMessage(self):
    if rollDice(event_constants.CHANCE_FOR_DM_SAVE):
      message = '{} saving throw'.format(random.choice(event_constants.SAVES))
    else:
      message = '{} check'.format(random.choice(event_constants.ABILITIES))
    if rollDice(event_constants.CHANCE_FOR_DM_SPECIAL):
      message += ' ' + random.choice(event_constants.SPECIAL)
    if message.startswith(event_constants.VOWELS):
      message = 'an {}'.format(message)
    else: 
      message = 'a {}'.format(message)
    return message
