from bots._bot import Bot

class Code(Bot):
  
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    if self._event.isFromABot() or not self._event.isAMessage():
      return
    
    doc = self._mongoUtil.findOne('bots', {'name': 'code'})
    target = doc['target']
    frequency = doc['frequency']
    
    if not self._event.isFrom(target) or not self._randomUtil.rollDice(frequency):
      return
    
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    identity = IDENTITIES[USERS[self._target.lower()]]
    self._postUtil.addMessage('Hi {}'.format(target), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    
    # self._postUtil.addMessage(frequency, self._event.channel(), self._event.threadId())
    # self._postUtil.addMessage(target, self._event.channel(), self._event.threadId())
    
    
    
    # if self._event.isFromABot() or not self._event.isFrom(target) or not self._randomUtil.rollDice(frequency) or not self._event.isAMessage():
    #   return
    # doc = self._mongoUtil.findOne('bots', {'name': 'code'})
    # frequency = doc['frequency']
    # self._postUtil.addMessage(frequency, self._event.channel(), self._event.threadId())
    # return