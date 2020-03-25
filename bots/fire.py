from constant.people import USERS
from model.identity import Identity
from bots._bot import Bot

class Fire(Bot):
  
  _active = True
  _frequency = .05
  _frequencyFire = .6
  _frequencyDrew = .2
  _target = 'Dakota'
  _ping = 'Drew'
  
  @classmethod
  def description(cls):
    return "`Fire` Has a {}% chance to say Pandora or Prometheus things when {} posts. {}% chance to also ping {}".format(cls._frequency * 100, cls._target, cls._frequencyDrew * 100, cls._ping)
    
  def run(self):
    if not self._event.isFrom(self._target) or self._event.isPartOfAThread() or self._event.isFromABot() or not self._event.isAMessage():
      return
    if not self._randomUtil.rollDice(self._frequency):
      return
    if self._randomUtil.rollDice(self._frequencyFire):
      message = 'Dakota gave us fire'
    else:
      message = 'Dakota opened the box'
    if self._randomUtil.rollDice(self._frequencyDrew):
      message = message + ' ' + self._identityUtil.pingUser(USERS[self._ping.lower()])
    
    self._postUtil.addMessageToThread(message, Identity(profilePicture = self._identityUtil.randomImageUrl()))
      