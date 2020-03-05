import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity
import re

class ContractionJunction(Bot):

  _frequency = 1
  # _target = 'Brenden'
  
  
  _before = {
    "am": "m",
    "are": "re",
    "does": "es",
    "is": "s",
    "has": "as",
    "have": "ve",
    "had": "ad",
    "did": "id",
    "would": "d",
    "will": "ll",
    "shall": "all",
    "them": "em"
  }
  
  
  _contractions={"not":"n't","am":"'m","are":"'re","does":"'s","is":"'s","has":"'s","have":"'ve","had":"'d","did":"'d",
              "would":"'d","will":"'ll","shall":"'ll","them":"'em"}
  _next={"it":"'t","of":"o'","of the":"o'","you":"y'"}
  _full={"I am":"I'm","let us":"let's"}
  message=""
  @classmethod
  def description(cls):
    return "`contraction_junction` has a {}% chance to contract {}'s message".format(cls._frequency * 100, cls._target)
    
  def run(self):
    # if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFromChaosUser() or not self._randomUtil.rollDice(self._frequency) or not self._event.isInChannel("Megamoji"):
    #   return
    if self._event.isFromABot() or not self._event.isAMessage() or not self._randomUtil.rollDice(self._frequency) or not self._event.isInChannel("Megamoji"):
      return
    
    message = self._event.text()
    for i in self._before:
      regex = r'(\s{1}' + i + r')|(\b' + i + r')'
      # message = re.sub(regex, "'" + self._before[i], message)
      message = re.sub(regex, "'" + self._before[i], message, flags=re.IGNORECASE)
    # for i in self._contractions:
    #   message = message.lower().replace(f" {i} ", f"{self._contractions[i]} ")
    # for i in self._next:
    #   message = message.lower().replace(f" {i} ", f" {self._next[i]}")
    # for i in self._full:
    #   message = message.lower().replace(i, self._full[i])
      
    print(message)

    if message == self._event.text().lower():
      return
    
    identity = IDENTITIES[self._event.user()]
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    self._postUtil.addMessage(message, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    return
