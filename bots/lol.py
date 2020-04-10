from bots._bot import Bot

class Lol(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "Adds an emote if your message matches an emote"
  
  def run(self):
    if not self._event.text() or not self._event.isAMessage():
      return
    
    if self._event.text() == 'q w':
      self._postUtil.addReactionToMessage('lol')
      return
    
    emojis = self._emoteUtil.getAll()
    if self._event.text().lower() in emojis: 
      self._postUtil.addReactionToMessage(self._event.text().lower())
