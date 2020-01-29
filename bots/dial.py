import random
from model.identity import Identity
from bots._bot import Bot
from constant.channels import CHANNELS

class Dial(Bot):
  
  def run(self):
    if self._event.user() != 'UDL020K8D' or self._event.channel() != 'CT98UFG80':
      return
    identity = Identity(emoji = 'musical_note');
    self._postUtil.addMessageToChannel(self._event.text(), CHANNELS['Chaos'], identity)