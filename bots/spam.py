from bots.bot import Bot
import os
import requests
import random
import urllib

class Spam(Bot):
  
  _frequency = .01
  _numberOfEmotes = 23
  
  @classmethod
  def description(cls):
    return "`Spam` Has a {}% chance to post {23} random reactions to a message".format(cls._frequency * 100, cls._numberOfEmotes)
  
  def run(self):
    if not self._randomUtil.rollDice(self._frequency):
      return
    
    # this needs to be moved to util
    postData = {
      'token': os.environ.get('SECRET')
    }
    req = requests.get('https://slack.com/api/emoji.list?{}'.format(urllib.parse.urlencode(postData)))
    
    for i in range(1, self._numberOfEmotes):
      self._postUtil.addReaction(random.choice(list(req.json().get('emoji').keys())), self._event.channel(), self._event.id())