from bots._bot import Bot
from googletrans import Translator

class Greek(Bot):
  
  _frequency = .01
  
  def run(self):
    if not self._chaosUserSendsMessage() or not self._randomUtil.rollDice(self._frenquency):
      return
    
    translator = Translator()
    thing = translator.translate(self._event.text(), dest='el')
    print(thing)