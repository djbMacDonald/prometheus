import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity

class contraction_junction(Bot):

  _frequency = 1
  _target = 'Brenden' 
  _contractions={"not":"n't","am":"'m","are":"'re","does":"'s","is":"'s","has":"'s","have":"'ve","had":"'d","did":"'d",
              "would":"'d","will":"'ll","shall":"'ll","of":"o'","of the":"o'","it":"'t","them":"'em","you":"y'",
              "I am":"I'm","let us":"let's"}
  
  @classmethod
  def description(cls):
    return "`contraction_junction` has a {}% chance to contract {}'s message".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom(self._target):
      return
    if  self._randomUtil.rollDice(self._frequency):
      
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[self._target.lower()]]
      self._postUtil.addMessage(' '.join(words), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get))
      return
