import random
from bots._bot import Bot
import re

class Contraction(Bot):

  _active = True
  _frequency = .05
  
  _inner = {
    "you all": "y'all",
    "over": "o'er",
    "ever": "e'er",
    "never": "ne'er",
    "yes": "yup",
    "actually": "act'ly",
    "when": "w'en",
    "even": "e'en"
  }
  
  _inner_upper = {
    "Of the": "O'",
    "You all": "Y'all",
    "Over": "O'er",
    "Ever": "E'er",
    "Never": "Ne'er",
    "Yes": "Yup",
    "Actually": "Act'ly",
    "When": "W'en",
    "Even": "E'en"
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
    "it": "t",
    "instead": "stead",
    "not": "nt",
    "at": "t",
    "him": "im",
    "her": "er"
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
    return "Has a {}% chance to turn a message to contractions".format(cls._frequency * 100)
    
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
      message = re.sub(f'(\.\\s{i}\\b)', f'. \'{self._before[i]}', message, flags = re.IGNORECASE)
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
    
    self._replacePost(message)
    return
