from bots._bot import Bot
from googletrans import Translator

class Greek(Bot):
  
  _active = True
  _frequency = .01
  
  def run(self):
    if not self._event.isInChannel('Megamoji') or not self._event.text() or not self._event.isAMessage():
      return
    
    # if not self._chaosUserSendsMessage() or not self._randomUtil.rollDice(self._frenquency):
    #   return
    
    translator = Translator()
    thing = translator.translate(self._event.text(), dest='el')
    print(thing)
    print(thing.get('text'))