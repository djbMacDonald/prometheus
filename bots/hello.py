from utils.post import PostUtil
import random
import requests

class HelloBot:
  
  @classmethod
  def description(cls):
    return "`Name bot` ".format()
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
  
  def run(self):
    if self._event.text() and self._event.text().lower() == "hi prometheus":
      self._postUtil.addMessageToChannel('Hello!', self._event.channel())