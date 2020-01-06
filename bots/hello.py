import random
from bots.bot import Bot

class Hello(Bot):
  
  @classmethod
  def description(cls):
    return "`Hello` if you say 'Hi Prometheus' it will say hello back."
  
  def run(self):
    if self._event.text() and self._event.text().lower() == "hi prometheus":
      self._postUtil.addMessageToChannel('Hello!', self._event.channel())