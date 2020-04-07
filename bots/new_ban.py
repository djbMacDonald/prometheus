from bots._bot import Bot

class NewBan(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    if not self._event.isInChannel('Secret') or not self._event.text() == 'new ban':
      return
    self._banUtil.banNewWord()
  