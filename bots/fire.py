from utils.post import PostUtil
from utils.identity import IdentityUtil
from utils.random import RandomUtil
from constant.people import USERS

class FireBot():
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFrom('Dakota') and not self._event.isPartOfAThread():
      return
    if not self._randomUtil.rollDice(1/10):
      return
    if self._randomUtil.rollDice(6/10):
      message = 'Dakota gave us fire'
    else:
      message = 'Dakota opened the box'
    if self._randomUtil.rollDice(2/10):
      message = message + ' ' + self._identityUtil.pingUser(USERS['drew'])
    
    self._postUtil.addMessageToThread(message, self._event.channel(), self._event.id(), Identity(profilePicture = self._identityUtil.randomImageUrl()))
      