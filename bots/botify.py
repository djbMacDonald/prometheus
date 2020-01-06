from utils.post import PostUtil
import random
from model.identity import Identity
import requests
from utils.random import RandomUtil
from constant.people import USERS, IDENTITIES

class BotifyBot:
  
  _frequency = .2
  _target = "CJ"
  
  @classmethod
  def description(cls):
    return "`Botify` Has a {}% chance of replacing {}'s message with {}-bot's message".format(cls._frequency * 100, cls._target, cls._target)
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
  
  def run(self):
    if self._event.isAMessage() and self._event.isFrom(self._target) and self._randomUtil.rollDice(self._frequency):
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[self._event.user()]
      self._postUtil.addMessage(self._event.text(), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))