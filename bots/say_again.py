import random
from model.identity import Identity
import json
from constant.people import IDENTITIES
from bots.bot import Bot

class SayAgainBot(Bot):
  
  @classmethod
  def description(cls):
    return "`Say Again` If you say 'you can say that again', it will say it again"
  
  def run(self):
    if not self._event.text() or self._event.isFromABot() or not self._event.text().lower() == "you can say that again":
      return
    if self._event.isPartOfAThread():
      threadJson = self._channelUtil.getThreadData(self._event.threadId(), self._event.channel())
      messages = reversed(threadJson['messages'])
    else:
      threadJson = getChannelData(self._event.channel())
      messages = threadJson['messages']
      
    messageText = ''
    for message in messages:
      if message['text'].lower() != 'you can say that again' and message.get('user'):
        self._postUtil.addMessage(
          message['text'], 
          self._event.channel(), 
          self._event.threadId(), 
          identity = Identity(IDENTITIES[user].get('username'), IDENTITIES[user].get('profilePicture'))
        )