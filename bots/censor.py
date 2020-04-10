from model.identity import Identity
import re
from bots._bot import Bot

class Censor(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "Censors instances of banned words. Only applies to those opted into Chaos Users. The banned word changes every day."
  
  def run(self):
    if not self._event.isFromChaosUser():
      return
    
    if not self._event.text() or self._event.isFromABot():
      return
    
    bans = self._banUtil.getBans()
    activeBans = self._banUtil.activeBans(bans)

    if len(activeBans) == 0:
      bans = self._banUtil.banNewWord();
    self._censorMessage(activeBans);
    
  def _censorMessage(self, bans):
    newMessage = self._event.text()
    words = newMessage.split(' ');
    for i in range(0, len(words)):
      words[i] = '~*REDACTED*~'
    fullRedaction = ' '.join(words);
    if ('cj' in bans.keys() and self._event.isFrom('cj')):
        #do nothing
        self._postUtil.replacePost(fullRedaction)
        return
    
    newMessage = self._event.text();
    for ban in bans.keys():
      if (not isinstance(ban, str)) or 'redacted' in ban.lower() or not ban.isalpha():
        continue
      newMessage = re.sub(r'\b[^A-Za-z0-9]?({})[^A-Za-z0-9]?\b'.format(ban), ' ~*REDACTED*~ ', newMessage, flags=re.IGNORECASE)
    for ban in bans.keys():
      if (not isinstance(ban, str)) or 'redacted' in ban.lower() or not ban.isalpha():
        continue
      newMessage = re.sub(r'\b[^A-Za-z0-9]?({})[^A-Za-z0-9]?\b'.format(ban), ' ~*REDACTED*~ ', newMessage, flags=re.IGNORECASE)
    if self._event.text() == newMessage:
      return;
    self._postUtil.replacePost(newMessage)