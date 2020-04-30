import random
from model.identity import Identity
from bots._bot import Bot
from constant.channels import chaosChannel

class Dial(Bot):
  
  _active = True
  
  def run(self):
    if self._event.channel() != 'CSZFZKGFK' or self._event.isFromABot() or not self._event.isAMessage():
      return
    identity = Identity(userName = 'The Singer', emoji = 'musical_note');
    self._addMessageToChannel(self._event.text(), identity, chaosChannel())