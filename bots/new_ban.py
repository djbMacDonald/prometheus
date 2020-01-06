from bots.bot import Bot

class NewBanBot(Bot):
  
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    if not self._event.isInChannel('Secret') or not self._event.text() == 'new ban':
      return
    self._banUtil.banNewWord()
  