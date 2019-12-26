from utils.post_util import PostUtil
import random
from identity import Identity
import os
import urllib
import requests

class HelloBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
  
  def run(self):
    if self._event.text().lower() == "hi prometheus":
      self._postUtil.addMessageToChannel('Hello!', self._event.channel())