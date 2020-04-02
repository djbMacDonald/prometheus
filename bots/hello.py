import random
from bots._bot import Bot

class Hello(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "`Hello` if you say 'Hi Prometheus' it will say hello back."
  
  def run(self):
    if self._event.text() and self._event.text().lower() == "hi prometheus":
      self._postUtil.addMessageToChannel('Hello!')