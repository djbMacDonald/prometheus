from utils.post_util import PostUtil
import random
from identity import Identity
import os
import urllib
import requests
from utils.random import RandomUtil
from utils.identity import IdentityUtil

class DejaVuBot:
  
  _frequency = .01
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
    self._identityUtil = IdentityUtil()
  
  def run(self):
    a = 5
    if self._event.isFromABot() or not self._randomUtil.rollDice(self._frequency):
      return
    lines = open('{}_logfile.txt'.format(self.channel), 'r').read().splitlines()
    self._postUtil.addReaction('dejavu', self._event.channel(), self._event.id())
    myline = random.choice(lines)
    self._postUtil.addMessage(myline, self._event.channel(), self._event.threadId(), identity = self._identityUtil.getRandomIdentity())
    #Drew says don't clear the file. What a Jerk
    #self.logToNewFile()
