from bots._bot import Bot

class Code(Bot):
  
  @classmethod
  def description(cls):
    return "`Code` sort of a test to get configs from DB. Eventually I need to allow these comments to view settings as well."
  
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage():
      return
    
    doc = self._mongoUtil.findOne('bots', {'name': 'code'})
    target = doc['target']
    frequency = int(doc['frequency'])
    
    if not self._event.isFrom(target) or not self._randomUtil.rollDice(frequency):
      return
    
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    identity = IDENTITIES[USERS[self._target.lower()]]
    self._postUtil.addMessage('`{}`'.format(self._event.text()), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))