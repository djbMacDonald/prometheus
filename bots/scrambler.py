import random

from util.random import RandomUtil
from util.message import MessageUtil

from constants.people import IDENTITIES, USERS

class ScramblerBot:
  
  _frequency = 1/10
  _user = 'drew'
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._messageUtil = MessageUtil(pool)
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(_user):
      return
    words = self._event.text().split(' ')
    if len(words) > 1 and self._randomUtil.rollDice(self._frequency):
      random.shuffle(words)
      self._messageUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[_user]]
      self._messageUtil.addMessage(' '.join(words), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
      return
