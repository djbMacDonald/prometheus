import random

from util.random import RandomUtil
from util.message import MessageUtil

class ScramblerBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom('Drew'):
      return
    words = self._event.text().split(' ')
    if len(words) > 1 and rollDice(event_constants.CHANCE_FOR_REPLACEMENT_BOT/10):
      random.shuffle(words)
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = event_constants.IDENTITIES[event_constants.USERS[user]]
      self._postUtil.addMessage(' '.join(words), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
      return
