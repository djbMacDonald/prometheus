from utils.post import PostUtil
from utils.identity import IdentityUtil
from utils.random import RandomUtil
from constant.people import USERS
from model.identity import Identity

class FireBot():
  
  _frequency = .1
  _frequencyFire = .6
  _frequencyDrew = .2
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFrom('Dakota') and not self._event.isPartOfAThread() and not self._event.isFromABot():
      return
    if not self._randomUtil.rollDice(self._frequency):
      return
    if self._randomUtil.rollDice(self._frequencyFire):
      message = 'Dakota gave us fire'
    else:
      message = 'Dakota opened the box'
    if self._randomUtil.rollDice(self._frequencyDrew):
      message = message + ' ' + self._identityUtil.pingUser(USERS['drew'])
    
    self._postUtil.addMessageToThread(message, self._event.channel(), self._event.id(), Identity(profilePicture = self._identityUtil.randomImageUrl()))
      