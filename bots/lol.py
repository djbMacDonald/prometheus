from bots._bot import Bot

class Lol(Bot):
  
  @classmethod
  def description(cls):
    return "`Lol` Adds an emote if your message matches an emote"
  
  def run(self):
    if not self._event.text():
      return
    emojis = self._emoteUtil.getAll()
    if self._event.text().lower() in emojis: 
      self._postUtil.addReactionToMessage(self._event.text().lower())