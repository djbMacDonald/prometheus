from bots._bot import Bot

class Lol(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "Adds an emote if your message matches an emote"
  
  def run(self):
    if not self._event.text() or not self._event.isAMessage():
      return
    
    emojis = self._emoteUtil.getAll()
    if self._event.text().lower() in emojis: 
      self._addReactionToMessage(self._event.text().lower())
