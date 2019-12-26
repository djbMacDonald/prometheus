from utils.post_util import PostUtil
import random
from identity import Identity
import os
import urllib
import requests
import json
from utils.channel import ChannelUtil
from constants.people import IDENTITIES

class SayAgainBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._channelUtil = ChannelUtil()
  
  def run(self):
    if self._event.isFromABot() or not self._event.text().lower() == "you can say that again":
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