from utils.post import PostUtil
import random
from model.identity import Identity
from utils.random import RandomUtil
from constant.dungeon import ABILITIES, SAVES, SPECIAL, ACTIONS, DANGERS
from constant.language import VOWELS

class DmBot:
  
  _frenquency = .02
  _frequency_save = .2
  _frequency_special = .2
  
  @classmethod
  def description(cls):
    return "`DM bot` Has a {}% chance to post a command from your dungeon master. {}% of the time it will be a saving throw. A".format()
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFromABot()or self._event.isPartOfAThread():
      return;
    if self._randomUtil.rollDice(self._frenquency):
      message = 'Roll {} to {} the {}'.format(self._createRollMessage(), random.choice(ACTIONS), random.choice(DANGERS))
      identity = Identity(userName = 'Dungeon Master')
      if self._event. isPartOfAThread():
        self._postUtil.addMessageToThread(message, self._event.channel(), self._event.id(), identity)
      else:
        self._postUtil.addMessageToChannel(message, self._event.channel(), identity)
        
  def _createRollMessage(self):
    if self._randomUtil.rollDice(self._frequency_save):
      message = '{} saving throw'.format(random.choice(SAVES))
    else:
      message = '{} check'.format(random.choice(ABILITIES))
    if self._randomUtil.rollDice(self._frequency_special):
      message += ' ' + random.choice(SPECIAL)
    if message.startswith(VOWELS):
      message = 'an {}'.format(message)
    else: 
      message = 'a {}'.format(message)
    return message
