from utils.post import PostUtil
import random
from model.identity import Identity
import requests
from utils.random import RandomUtil
from constant.people import USERS, IDENTITIES

class SpaceReplaceBot:
  
  _frequency = .01
  _target = 'Brenden'
  
  @classmethod
  def description(cls):
    return "`Space Replace bot` Has a {}% chance to replace {}'s spaces with dashes".format(cls._frequency * 100, cls._target)
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
  
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target) or not self._randomUtil.rollDice(self._frequency):
      return
    if ' ' in self._event.text():
      message = self._event.text().replace(' ', '-')
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[user]]
      self._postUtil.addMessage(message, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
      return