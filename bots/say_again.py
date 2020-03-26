import random
from model.identity import Identity
import json
from constant.people import IDENTITIES
from bots._bot import Bot

class SayAgain(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "`Say Again` If you say 'you can say that again', it will make someone say it again."
  
  def run(self):
    return #OFF
    if not self._event.text() or self._event.isFromABot() or not self._event.text().lower() == "you can say that again" or not self._event.isInChannel('Megamoji'):
      return
    if self._event.isPartOfAThread():
      threadJson = self._channelUtil.getThreadData(self._event.threadId(), self._event.channel())
      print(threadJson)
      messages = reversed(threadJson['messages'])
    else:
      threadJson = self._channelUtil.getChannelData(self._event.channel())
      messages = threadJson['messages']
    
    identity = IDENTITIES[self._event.user()]
    messageText = ''
    for message in messages:
      if message['text'].lower() != 'you can say that again' and message.get('user'):
        if not self._event.isPartOfAThread():
          if message.get('thread_ts'):
            continue;
          
        return self._postUtil.addMessage(message['text'], identity = Identity(identity.get('username'), identity.get('profilePicture')))
          