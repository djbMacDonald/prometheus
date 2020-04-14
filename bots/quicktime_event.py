import os
from bots._bot import Bot
import urllib
import requests
from utils.log import Log

class QuicktimeEvent(Bot):
  
  _active = True
  
  # @classmethod
  # def description(cls):
  #   return "`Pig` Has a {}% chance of replacing {}'s message with pig latin".format(cls._frequency * 100, cls._target)
  
  def run(self):
    
    if not self._event.isFrom('cja'): #or not self._event.isInChannel('Secret'):
      return
#     todo move to action queue probably
    postData = {
      'channel': self._event.channel(),
      'as_user': False,
      'user': self._event.user(),
      'username': 'WARNING',
      'icon_emoji': ':warning:',
      'text': 'DODGE!',
      'attachments': [
        {
          "callback_id": "quicktime",
          "attachment_type": "default",
          "text": '',
          "fallback": "Well this is awkward :bug:",
          "actions": [{
            "name": "game",
            "text": "Dive",
            "style": "danger",
            "type": "button",
            "value": "dive"
          }]
        }
      ],
      'token': os.environ.get('SECRET')

    }
    self._log = Log()
    self._pool = Pool(1)
    url = 'https://www.slack.com/api/chat.postEphemeral?{}'.format(urllib.parse.urlencode(postData))
    self._log.logEvent("{}: {}-bot makes an ephemeral post".format(self._event.channelName(), 'QuicktimeEvent'))
    self._pool.apply_async(requests.get, args=[url], callback=())
    return