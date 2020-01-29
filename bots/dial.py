import random
from model.identity import Identity
from bots._bot import Bot
from constant.channels import CHANNELS

class Dial(Bot):
  
  def run(self):
    print(self._event.user())
    print(self._event.channel())
    if self._event.user() != 'ULLQNJ8LX' or self._event.channel() != 'GT8N4T6KW':
      return
    identity = Identity(emoji = 'cj');
    self._postUtil.addMessageToChannel(self._event.text(), CHANNELS['Megamoji'], identity)