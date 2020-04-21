from bots._bot import Bot
from googletrans import Translator
import re

class Greek(Bot):
  
  _active = True
  _frequency = .01
  
  @classmethod
  def description(cls):
    return "Has a {}% chance to replace a word in the post with Greek, via Google Translate.".format(cls._frequency * 100)
  
  def run(self):
    if not self._chaosUserSendsMessage() or not self._randomUtil.rollDice(self._frenquency):
      return
    
    translator = Translator()
    
    words = re.findall(r'\w+', self._event.text())
    longWord = max(words, key=len)
    translation = translator.translate(longWord, dest='el').text
    if translation == longWord:
      return
    newString = self._event.text().replace(longWord, "{} [[{}]]".format(translation, longWord))
    self._replacePost(newString)