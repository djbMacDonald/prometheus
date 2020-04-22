from bots._bot import Bot
from googletrans import Translator
import re
import random

class Greek(Bot):
  
  _active = True
  _frequency = .01
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
    newString = self._event.text().replace(longWord, '{} [[{}]]', translation.text), longWord
    newString += '\n\n [[{}'.format(lang[1])
    if translation.pronunciation:
      newString += ' {}'.format(translation.pronunciation)
    newString += ']]'
    self._replacePost(newString)