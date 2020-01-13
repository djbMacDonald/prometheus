import random
from model.identity import Identity
from constant.language import VOWELS
from constant.people import USERS, IDENTITIES
from bots._bot import Bot

class Pig(Bot):
  
  _frequency = .0025
  _target = 'CJ'
  
  @classmethod
  def description(cls):
    return "`Pig` Has a {}% chance of replacing {}'s message with pig latin".format(cls._frequency * 100, cls._target)
  
  def run(self):
    if self._event.isFromABot() or not self._event.isFrom(self._target) or not self._randomUtil.rollDice(self._frequency) or not self._event.isAMessage():
      return;
    text = [i for i in self._event.text()]
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
    identity = IDENTITIES[USERS[self._target.lower()]]
    self._postUtil.addMessage(' '.join(text), self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    return
