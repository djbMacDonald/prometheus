from model.identity import Identity
from bots._bot import Bot

class Birthday(Bot):
  
  _active = False
  _frequency = .5
  _target = 'Brenden'
  
  @classmethod
  def description(cls):
    return "Has a {}% chance to say happy brithday on {}'s' posts".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if self._triggerUtil.targetSendsMessageToChannel(self._target, self._frequency):
      self._postUtil.addMessageToThread(':party: Happy Birthday {} :party:'.format(self._target), Identity(profilePicture = self._identityUtil.randomImageUrl()))