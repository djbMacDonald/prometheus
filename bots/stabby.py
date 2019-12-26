from utils.post import PostUtil
import random
import os
import requests

class StabbyBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._pool = pool
    self._postUtil = PostUtil(pool)
    
  def run(self):
    if self._event.isAMessage() and 'stabby' in self._event.text().lower() and self._event.isFrom('CJ'):
      self._postUtil.addMessageToThread(':rip: Capitan Stabby Reactji :rip:', self._event.channel(), self._event.id())