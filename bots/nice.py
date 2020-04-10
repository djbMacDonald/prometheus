import random
from bots._bot import Bot
from constant.people import IMPERSONATIONS
from model.identity import Identity

class Nice(Bot):
  
  _active = True
  _min = 3
  _max = 10
  
  @classmethod
  def description(cls):
    return "If you say nice, will respond with 'nice', {} to {} times".format(cls._min, cls._max)
  
  def run(self):
    if self._event.isFromABot() or not self._event.text() or len(self._event.text()) < 1 or not self._event.text() == 'nice' or  self._event.isPartOfAThread():
      return
    
    copy = IMPERSONATIONS
    random.shuffle(copy)
    
    for impersonation in copy:
      identity = Identity(identity.get('username'), identity.get('profilePicture'))
      self._postUtil.addMessageToThread('nice', identity)