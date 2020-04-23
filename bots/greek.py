from bots._bot import Bot
from googletrans import Translator
import re
import random

class Greek(Bot):
  
  _active = True
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
    # if not self._chaosUserSendsMessage() or not self._randomUtil.rollDice(self._frequency):
    #   return
    if not self._event.isInChannel('Megamoji') or self._event.isFromABot() or not self._event.isAMessage() or not self._event.isFrom('Doug'):
      return
    
    translator = Translator()
    
    originalString = str(self._event.text())
    
    words = re.findall(r'\w+', originalString)
    
    cool = False
    while not cool and len(words) > 0:
      longWord = max(words, key=len)
      charBefore = self.getCharacterBefore(longWord, originalString)
      charAfter = self.getCharacterAfter(longWord, originalString)
      if (
        charAfter is not '@' and
        (charBefore is not ':' and charAfter is not ':')
      ):
        cool = True
      words.remove(longWord)
    if not cool:
      return
    
    lang = random.choice(list(self._langauges.items()))
    translation = translator.translate(longWord, dest=lang[0])
    if translation.text == longWord:
      return
    newString = originalString.replace(longWord, '{} [[{}]]'.format(translation.text, longWord))
    newString += '\n\n [[{}'.format(lang[1])
    if translation.pronunciation:
      newString += ': {}'.format(translation.pronunciation)
    newString += ']]'
    self._replacePost(newString)
    
  def _isCharacterBefore(self, place):
    return place - 1 > 0   
  
  def _isCharacterAfter(self, place, length, string):
    return len(string) > place+length
  
  def getCharacterBefore(self, word, string):
    place = string.find(word)
    if not self._isCharacterBefore(place):
      return None
    return string[place - 1]

  def getCharacterAfter(self,word, string):
    place = string.find(word)
    length = len(word)
    if not self._isCharacterAfter(place, length, word):
      return None
    return string[place+length]