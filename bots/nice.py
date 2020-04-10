import random
from bots._bot import Bot
from constant.people import IMPERSONATIONS
from model.identity import Identity

class Nice(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "If you say nice, will respond with 'nice' for all impersonations"
  
  def run(self):
    if self._event.isFromABot() or not self._event.text() or len(self._event.text()) < 1 or not self._event.text() == 'nice' or  self._event.isPartOfAThread():
      return
    
    copy = IMPERSONATIONS
    random.shuffle(copy)
    
    for impersonation in copy:
      if self._event.user() == impersonation.get('id'):
        continue
      identity = Identity(impersonation.get('username'), impersonation.get('profilePicture'))
      self._postUtil.addMessageToThread('nice', identity)