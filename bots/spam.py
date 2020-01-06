from bots.bot import Bot
import os
import requests
import random
import urllib

class Spam(Bot):
  
  _frequency = .01
  
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    if self._event.isPartOfAThread() or not self._randomUtil.rollDice(self._frequency) or not self._event.text() == "spam50":
      return
    
    # this needs to be moved to util
    postData = {
      'token': os.environ.get('SECRET')
    }
    req = requests.get('https://slack.com/api/emoji.list?{}'.format(urllib.parse.urlencode(postData)))
    
    for i in range(1, 50):
      self._postUtil.addReaction(random.choice(list(req.json().get('emoji').keys())), self._event.channel(), self._event.id())