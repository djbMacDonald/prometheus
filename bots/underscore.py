import random
from bots._bot import Bot

class Underscore(Bot):
  
  _active = True
  
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
      self._replacePost(text)
    return
