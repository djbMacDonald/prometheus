from bots._bot import Bot
from model.identity import Identity

class Code(Bot):
  
  @classmethod
  def description(cls):
    return "`Code` sort of a test to get configs from DB. Eventually I need to allow these comments to view settings as well."
  
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage():
      return
    
#     it is possible to fetch all settings in a single call. This needs to be refactored to that model before people copy this code.
#     doc = self._mongoUtil.findOne('bots', {'name': 'code'})
#     target = doc['target']
#     frequency = float(doc['frequency'])
    
#     if not self._event.isFrom(target) or not self._randomUtil.rollDice(frequency):
#       return
    
#     self._postUtil.replacePost(self._event, '`{}`'.format(self._event.text()))