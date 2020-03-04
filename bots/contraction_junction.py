import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity

class ContractionJunction(Bot):

  _frequency = .15
  _target = 'Brenden' 
  _contractions={"not":"n't","am":"'m","are":"'re","does":"'s","is":"'s","has":"'s","have":"'ve","had":"'d","did":"'d",
              "would":"'d","will":"'ll","shall":"'ll","them":"'em"}
  _next={"it":"'t","of":"o'","of the":"o'","you":"y'"}
  _full={"I am":"I'm","let us":"let's"}
  message=""
  @classmethod
  def description(cls):
    return "`contraction_junction` has a {}% chance to contract {}'s message".format(cls._frequency * 100, cls._target)
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFromChaosUser():
      return
    if  self._randomUtil.rollDice(self._frequency):
      message=self._event.text()
      for i in self._contractions:
        message=message.lower().replace(f" {i} ",f"{self._contractions[i]} ")
      for i in self._next:
        message=message.lower().replace(f" {i} ",f" {self._next[i]}")
      for i in self._full:
        message=message.lower().replace(i,self._full[i])
        
      if message==self._event.text().lower():
        return
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[self._event.user()]
      self._postUtil.addMessage(message, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
      return
