import random
from model.identity import Identity
from constant.dungeon import ABILITIES, SAVES, SPECIAL, ACTIONS, DANGERS
from constant.language import VOWELS
from bots._bot import Bot

class Dm(Bot):
  
  _frenquency = .01
  _frequency_save = .2
  _frequency_special = .2
  
  @classmethod
  def description(cls):
    return "`DM` Has a {}% chance to post a command from your dungeon master. {}% of the time it will be a saving throw. Only works on messages in channel directly.".format(cls._frenquency * 100, cls._frequency_save * 100)
    
  def run(self):
    if self._event.isFromABot() or self._event.isPartOfAThread() or not self._event.isAMessage() or not self._randomUtil.rollDice(self._frenquency):
      return;
    message = 'Roll {} to {} the {}'.format(self._createRollMessage(), random.choice(ACTIONS), random.choice(DANGERS))
    identity = Identity(userName = 'Dungeon Master', profilePicture = self._identityUtil.randomImageUrl())
    self._postUtil.addMessageToChannel(message, identity)
        
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
