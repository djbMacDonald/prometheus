from constant.people import USERS
from model.identity import Identity
from bots._bot import Bot

class Crabby(Bot):
  
  _frequency = .99
  _target = 'Ayshu'
  
  @classmethod
  def description(cls):
    return "`Crabby` Has a {}% chance to let people know {} is crabby".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if not self._event.isFrom(self._target) or self._event.isPartOfAThread() or self._event.isFromABot():
      return
    if not self._randomUtil.rollDice(self._frequency):
      return
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    identity = IDENTITIES[self._event.user()]
    self._postUtil.addMessage(f":crab: {self._event.text()} :crab:", self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
      