import random
import os
from model.identity import Identity
from constant.language import VOWELS
from constant.people import USERS, IDENTITIES
from bots._bot import Bot

class QuicktimeEvent(Bot):
  
  
  # @classmethod
  # def description(cls):
  #   return "`Pig` Has a {}% chance of replacing {}'s message with pig latin".format(cls._frequency * 100, cls._target)
  
  def run(self):
    
    if not self._event.isFrom('Dakota') or not self._event.isInChannel('Secret'):
      return
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
            "text": "Done",
            "style": "danger",
            "type": "button",
            "value": "done"
          }]
        }
      ],
      'token': os.environ.get('SECRET')

    }
    self._postUtil.postEphemeral(postData)
    return