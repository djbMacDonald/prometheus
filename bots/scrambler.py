from utils.post import PostUtil
import random
from utils.random import RandomUtil
from constant.people import USERS, IDENTITIES

class ScramblerBot:
  
  _frequency = .1
  _target = 'Drew'
  
  @classmethod
  def description(cls):
    return "`Scrambler bot` Has a {}% chance to scramble {}'s message".format(cls._frequency * 100, cls._target)
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target):
      return
    words = self._event.text().split(' ')
    if len(words) > 1 and self._randomUtil.rollDice(self._frequency):
      random.shuffle(words)
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[user]]
      self._postUtil.addMessage(' '.join(words), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
      return
