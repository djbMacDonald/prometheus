from bots.bot import Bot

class Lol(Bot):
  
  @classmethod
  def description(cls):
    return "`Lol` Adds an emote if your message matches an emote"
  
  def run(self):
    if not self._event.text():
      return
    emojis = self._postUtil.getAllEmojis()
    if self._event.text().lower() in emojis: 
      self._postUtil.addReaction(self._event.text().lower(), self._event.channel(), self._event.id())