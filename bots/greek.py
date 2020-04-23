from bots._bot import Bot
from googletrans import Translator
import re
import random

class Greek(Bot):
  
  _active = False
  _frequency = .03
  _langauges = {
    'el': 'Greek',
    'te': 'Telegu',
    'ru': 'Russian',
    'iw': 'Hebrew',
    'fa': 'Farsi'
  }
  
  @classmethod
  def description(cls):
    return "Has a {}% chance to replace a word in the post with another language, via Google Translate.".format(cls._frequency * 100)
  
  def run(self):
    if not self._chaosUserSendsMessage() or not self._randomUtil.rollDice(self._frequency):
      return
    
    translator = Translator()
    
    words = re.findall(r'\w+', self._event.text())
    longWord = max(words, key=len)
    lang = random.choice(list(self._langauges.items()))
    translation = translator.translate(longWord, dest=lang[0])
    if translation.text == longWord:
      return
    newString = self._event.text().replace(longWord, '{} [[{}]]'.format(translation.text, longWord))
    newString += '\n\n [[{}'.format(lang[1])
    if translation.pronunciation:
      newString += ': {}'.format(translation.pronunciation)
    newString += ']]'
    self._replacePost(newString)
    
  def _isCharacterBefore(place):
    return place - 1 > 0   
  
  def _isCharacterAfter(place, length, string):
    return len(string) > place+length
  
  def getCharacterBefore(string, longWord):
    place = string.find(longWord)
    if not self._isCharacterBefore(place):
      return None
    return string[place - 1]

  def getCharacterAfter(thing, longWord):
    if not self._isCharacterAfter(thing, longWord):
      return None
    place = thing.find(longWord)
    length = len(longWord)
    return thing[place+length]