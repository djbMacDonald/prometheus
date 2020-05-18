from bots._bot import Bot

class Moogle(Bot):
  
  _active = False
  _target = 'Victoria'
  _frequency = 0
  
  _pronouns = ['you', 'me', 'i', 'they', 'them', 'him', 'her', 'he', 'she', 'it', 'we', 'me', 'us']
  
  @classmethod
  def description(cls):
    return "Makes {} talk like a moogle {}% of the time".format(cls._target, cls.frequency * 100)
  
  def run(self):
    if not self._targetSendsMessageToChannel():
      return
    newMessage = self._event.text()
    words = newMessage.split(' ');
    
