from utils.post import PostUtil
from constant.people import USERS, IDENTITIES
import random
from model.identity import Identity
import requests
from utils.ban import BanUtil
import re

class CensorBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._banUtil = BanUtil()
  
  def run(self):
    # if not self._event.isFromChaosUser():
    #   return
    
    if not self._event.text() or self._event.isFromABot():
      return
    
    bans = self._banUtil.getBans()
    activeBans = self._banUtil.activeBans(bans)
      
    print (bans)
    if len(activeBans) == 0:
      bans = self.banUtil._banNewWord();
    self._censorMessage(activeBans);
    
  def _censorMessage(self, bans):
    newMessage = self._event.text()
    words = newMessage.split(' ');
    for i in range(0, len(words)):
      words[i] = '~*REDACTED*~'
    fullRedaction = ' '.join(words);
    print(fullRedaction)
    if ('cj' in bans.keys() and self._event.isFrom('cj')):
        #do nothing
        text = fullRedaction
        print('banned!')
        self._postUtil.deleteMessage(self._event.channel(), self._event.id())
        identity = IDENTITIES[USERS[self._event.user()].lower()]
        self._postUtil.addMessage(text, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
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
    print ('NEW MESSAGE: ' + newMessage)
    if self._event.text() == newMessage:
      return;
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    identity = IDENTITIES[USERS[self._event.user()].lower()]
    self._postUtil.addMessage(newMessage, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))