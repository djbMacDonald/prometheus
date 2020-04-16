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
    self._addReactionToMessage('dejavu')
    myline = random.choice(lines)
    newId = self._identityUtil.getRandomIdentity()
    self._addMessage(myline, identity = newId)
    #Drew says don't clear the file. What a Jerk
    #self.logToNewFile()
