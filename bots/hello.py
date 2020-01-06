import random
from bots.bot import Bot

class HelloBot(Bot):
  
  @classmethod
  def description(cls):
    return "`Hello` if you say 'Hi Prometheus' it will say hello back."
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
  
  def run(self):
    if self._event.text() and self._event.text().lower() == "hi prometheus":
      self._postUtil.addMessageToChannel('Hello!', self._event.channel())