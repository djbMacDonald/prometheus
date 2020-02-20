from model.caster import Caster
from view.cast import CastView
from view.bot_list import BotListView
from view._view import View
import requests
import os
import json
import urllib
import view

class Modal:
  def __init__(self, type, req):
    
    botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(view))))
    print(botList)
    
    self.triggerId = req.get('trigger_id')
    
    if not self.triggerId:
      return
    
    #Build a Spell Cast ciew
    if type == 'cast':
      self.view = CastView(req).build()
      self.id = 'cast'

    if type == 'bot_list':
      self.view = BotListView(req).build()
      
      
  def open(self):
    if not self.view:
      return
    payload = {
      "token": os.environ.get('SECRET'),
      "trigger_id": self.triggerId,
      "state": 'Testing!',
      "view": self.view
    }
  
    url = 'https://slack.com/api/views.open'
    headers = {'content-type': 'application/json; charset=utf-8', "Authorization": f"Bearer {os.environ.get('SECRET')}"}
    req = requests.post(url, json.dumps(payload), headers=headers)
    res = req.json()
    print(res)
    return
    self.id = res.get('view').get('id')
    self.hash = res.get('view').get('hash')
    print(res)

  def update(self):
    if not self.view:
      return
    self.view = {
        "type": "modal",
        "title": {
          "type": "plain_text",
          "text": "Updated view"
        },
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "plain_text",
              "text": "I've changed and I'll never be the same. You must believe me."
            }
          }
        ]
      }
    payload = {
      "token": os.environ.get('SECRET'),
      'view_id': self.id,
      "view": self.view
    }
    url = 'https://slack.com/api/views.update?{}'.format(urllib.parse.urlencode(payload))
    res = requests.get(url)
    print(res.json())