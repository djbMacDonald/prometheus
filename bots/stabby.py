from bots._bot import Bot

class Stabby(Bot):
  
  _target = 'CJ'
  
  @classmethod
  def description(cls):
    return "`Stabby` If {} says 'stabby' then adds a reaction".format(cls._target)
    
  def run(self):
    if self._event.isAMessage() and 'stabby' in self._event.text().lower() and self._event.isFrom(self._target):
      self._postUtil.addMessageToThread(':rip: Capitan Stabby Reactji :rip:')