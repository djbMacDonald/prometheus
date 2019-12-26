from utils.post import PostUtil
import random
from model.identity import Identity
import os
import urllib
import requests
from utils.random import RandomUtil
from constant.language import VOWELS
from constant.people import USERS, IDENTITIES

class PigBot:
  
  _frequency = .01
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._randomUtil = RandomUtil()
  
  def run(self):
    user = 'cj'
    if self._event.isFromABot() or not self._event.isFrom(user) or not self._randomUtil.rollDice(self._frequency):
      return;
    text = [i for i in self._event.text]
    for i,letter in enumerate(text):
      # remove if not alpha, space
      if not letter.isalpha() and not letter in ' ':
        text[i] = ''
    text = ''.join(text)
    text = [i for i in text.split()]
    for i,word in enumerate(text):
      if not word.startswith(VOWELS):
        vowels = []
        for _,letter in enumerate(word):
          if letter in VOWELS:
            vowels.append(letter)
        if len(vowels) > 0:	
          word = word.partition(vowels[0])
          word = ''.join(word[1:]) + word[0]
      text[i] = word + 'ay'
    self._postUtil.deleteMessage(self._event.channel(), self._event.id())
    identity = IDENTITIES[USERS[user]]
    self._postUtil.addMessage(' '.join(text), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    return
