from bots._bot import Bot

class Code(Bot):
  
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    if self._event.isFromABot() or not self._event.isInChannel('Megamoji') or not self._event.text() == 'test':
      return
    doc = self._mongoUtil.findOne('bots', {'name': 'code'})
    frequency = doc['frequency']
    self._postUtil.addMessage(frequency, self._event.channel(), self._event.threadId())
    return