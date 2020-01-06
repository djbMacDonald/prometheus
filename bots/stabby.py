from utils.post import PostUtil
import random
import requests

class StabbyBot:
  
  _target = 'CJ'
  
  @classmethod
  def description(cls):
    return "`Stabby` If {} says 'stabby' then adds a reaction".format(cls._target)
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._pool = pool
    self._postUtil = PostUtil(pool)
    
  def run(self):
    if self._event.isAMessage() and 'stabby' in self._event.text().lower() and self._event.isFrom(self._target):
      self._postUtil.addMessageToThread(':rip: Capitan Stabby Reactji :rip:', self._event.channel(), self._event.id())