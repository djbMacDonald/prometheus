import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot

class Underscore(Bot):
  
  @classmethod
  def description(cls):
    return ""
    
  def _runConditition(self):
    return self._event.isInChannel('Underscore') and self._event.isFromChaosUser() and not self._event.isFromABot()
  
  def run(self):
    if not self._runConditition():
      return
    if ' ' in self.text:
      text = self._event.text().replace(' ', '-')
      self._postUtil.replacePost(text)
    return 'end'
