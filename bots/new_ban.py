from utils.post import PostUtil
import random
from model.identity import Identity
import requests
import time
from pytz import timezone
from utils.ban import BanUtil

class NewBanBot:
  
  @classmethod
  def description(cls):
    return "`Name bot` ".format()
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._banUtil = BanUtil()
  
  def run(self):
    if not self._event.isInChannel('Secret') or not self._event.text() == 'new ban':
      return
    self._banUtil.banNewWord()
  