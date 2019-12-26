from utils.post_util import PostUtil
import random
from identity import Identity
import os
import urllib
import requests
import time
from pytz import timezone
from utils.ban import BanUtil

class NewBanBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._banUtil = BanUtil()
  
  def run(self):
    if not self._event.isInChannel('Secret') or not self._event.text() == 'new ban':
      return
    self._banUtil.banNewWord()
  