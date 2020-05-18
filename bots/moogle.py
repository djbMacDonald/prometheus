from bots._bot import Bot
import re

class Moogle(Bot):
  
  _active = True
  _target = 'Doug'
  _frequency = 1
  
  _pronouns = ['you', 'me', 'i', 'they', 'them', 'him', 'her', 'he', 'she', 'it', 'we', 'me', 'us']
  
  @classmethod
  def description(cls):
    return "Makes {} talk like a moogle {}% of the time".format(cls._target, cls.frequency * 100)
  
  def run(self):
    if not self._targetSendsMessageToChannel():
      return
    newMessage = self._event.text()
    for pronoun in self._pronouns:
      newMessage = re.sub(r'\b{}\b'.format(pronoun), 'TEST', newMessage, flags=(re.MULTILINE | re.IGNORECASE))
    if self._event.text() == newMessage:
      return;
    self._replacePost(newMessage)
    
