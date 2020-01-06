from bots.bot import Bot

class Spam(Bot):
  
  _frequency = .01
  
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    if self._event.isPartOfAThread() or not self._randomUtil.rollDice(self._frequency):
      return
    for i in range(1, 50):
      return ""