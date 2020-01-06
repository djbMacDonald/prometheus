from bots.bot import Bot

class Lol(Bot):
  
  @classmethod
  def description(cls):
    return "`Lol` Adds a LOL emote when you LOL"
  
  def run(self):
    if not self._event.text() or self._event.text().lower() != 'lol':
      return
    self._postUtil.addReaction('lol', self._event.channel(), self._event.threadId())