from constant.people import USERS
from model.identity import Identity
from bots._bot import Bot

class Birthday(Bot):
  
  _frequency = .5
  _target = 'Brendean'
  
  @classmethod
  def description(cls):
    return "`Birthday` Has a {}% chance to say happy brithday on {}'s' posts".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if not self._event.isFrom(self._target) or self._event.isPartOfAThread() or self._event.isFromABot():
      return
    if not self._randomUtil.rollDice(self._frequency):
      return
    message=':party: Happy Birthday {} :party:'.format(self._target)
    
    self._postUtil.addMessageToThread(message, self._event.channel(), self._event.id(), Identity(profilePicture = self._identityUtil.randomImageUrl()))