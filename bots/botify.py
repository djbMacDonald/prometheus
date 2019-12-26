from utils.post import PostUtil
import random
from model.identity import Identity
import os
import urllib
import requests
from utils.random import RandomUtil
from constant.people import USERS, IDENTITIES

class BotifyBot:
  
  _frequency = .2
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
  
  def run(self):
    if self._event.isAMessage() and self._event.isFrom('cj') and self.randomUtil.rollDice(self._frequency):
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[self._event.user()].lower()]
      self._postUtil.addMessage(self._event.text(), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))