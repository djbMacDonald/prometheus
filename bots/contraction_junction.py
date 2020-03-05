import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity
import re

class ContractionJunction(Bot):

  _frequency = .05
  
  _inner = {
    "of the": "",
    "you all": "",
    "not": "",
    "over": "",
    "ever": "",
    "never": ""
  }
  
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
    "them": "em",
    "us": "s",
    "it": "t"
  }
  
  _after = {
    "of": "o",
    "you": "y",
  }
  
  _after_upper = {
    "Of": "O",
    "You": "Y",
  }
  
  _next={"it":"'t","of":"o'","of the":"o'","you":"y'"}
  _full={"I am":"I'm","let us":"let's"}
  message=""
  @classmethod
  def description(cls):
    return "`contraction_junction` has a {}% chance to turn a message to contractions".format(cls._frequency * 100)
    
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFromChaosUser() or not self._randomUtil.rollDice(self._frequency):
      return
    # if self._event.isFromABot() or not self._event.isAMessage() or not self._event.isInChannel("Megamoji"):
    #   return
    
    message = self._event.text()
    for i in self._before:
      message = re.sub(f'(\\s{i}\\b)|(\\b{i}\\b)', f'\'{self._before[i]}', message, flags=re.IGNORECASE)
    for i in 
    for i in self._next:
      message = message.lower().replace(f" {i} ", f" {self._next[i]}")
    for i in self._full:
      message = message.lower().replace(i, self._full[i])
      
    print(message)

    if message == self._event.text().lower():
      return
    
    identity = IDENTITIES[self._event.user()]
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    self._postUtil.addMessage(message, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    return
