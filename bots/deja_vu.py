import random
from model.identity import Identity
from bots._bot import Bot

class DejaVu(Bot):
  
  _active = True
  _frequency = .01
  
  @classmethod
  def description(cls):
    return "Has a {}% chance to post a message from the channel history as a random bot".format(cls._frequency * 100)
  
  def run(self):
    if self._event.isFromABot() or not self._randomUtil.rollDice(self._frequency) or not self._event.isAMessage():
      return
    lines = open('{}_logfile.txt'.format(self._event.channel()), 'r').read().splitlines()
    self._postUtil.addReactionToMessage('dejavu')
    myline = random.choice(lines)
    self._postUtil.addMessage(myline, identity = self._identityUtil.getRandomIdentity())
    #Drew says don't clear the file. What a Jerk
    #self.logToNewFile()
