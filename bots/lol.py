from bots._bot import Bot

class Lol(Bot):
  
  @classmethod
  def description(cls):
    return "`Lol` DISABLED -- Adds an emote if your message matches an emote"
  
  def run(self):
    return
    if not self._event.text():
      return
    emojis = self._postUtil.getAllEmojis()
    if self._event.text().lower() in emojis: 
      self._postUtil.addReactionToMessage(self._event.text().lower())