import random
from constant.people import USERS, IDENTITIES
from bots._bot import Bot
from model.identity import Identity
import re

class Contraction(Bot):

  _frequency = .05
  
  _inner = {
    "you all": "y'all",
    "not": "'nt",
    "over": "o'er",
    "ever": "e'er",
    "never": "ne'er",
    "yes": "yup"
  }
  
  _inner_upper = {
    "Of the": "O'",
    "You all": "Y'all",
    "Not": "'Nt",
    "Over": "O'er",
    "Ever": "E'er",
    "Never": "Ne'er",
    "Yes": "Yup"
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
    "of the": "o",
    "of": "o",
    "you": "y",
  }
  
  _after_upper = {
    "Of the": "O",    
    "Of": "O",
    "You": "Y",
  }
  
  @classmethod
  def description(cls):
    return "`contraction_junction` has a {}% chance to turn a message to contractions".format(cls._frequency * 100)
    
  def run(self):
    if (
        self._event.isFromABot() 
        or not self._event.isAMessage() 
        or not self._event.isFromChaosUser() 
        or not self._randomUtil.rollDice(self._frequency) 
        or self._event.isFrom('Ayshu')
    ):
      return
    
    message = self._event.text()
    
    for i in self._before:
      message = re.sub(f'(\\s{i}\\b)|(\\b{i}\\b)', f'\'{self._before[i]}', message, flags = re.IGNORECASE)
    for i in self._after_upper:
      message = re.sub(f'(\\b{i}\\s\')|(\\b{i}\')|(\\b{i}\\s)|(\\b{i}\\b)', f'{self._after_upper[i]}\'', message)
    for i in self._after:
      message = re.sub(f'(\\b{i}\\s\')|(\\b{i}\')|(\\b{i}\\s)|(\\b{i}\\b)', f'{self._after[i]}\'', message, flags = re.IGNORECASE)
    for i in self._inner_upper:
      message = re.sub(f'(\\b{i}\\b)', f'{self._inner_upper[i]}', message)
    for i in self._inner:
      message = re.sub(f'(\\b{i}\\b)', f'{self._inner[i]}', message, flags = re.IGNORECASE)

    if message == self._event.text():
      return
    
    identity = IDENTITIES[self._event.user()]
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    self._postUtil.addMessage(message, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    return
