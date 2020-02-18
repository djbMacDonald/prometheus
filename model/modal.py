from model.caster import Caster
from view.cast import CastView
import requests
import os
import urllib
import view

class Modal:
  def __init__(self, type, req):
    
    botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(view))))
    print(botList)
    
    self.triggerId = req.get('trigger_id')
    self.header = {"type": "modal"}
    
    if not self.triggerId:
      return
    
    #Build a Spell Cast ciew
    if type == 'cast':
      caster = Caster(req.get('user_id'))
      castView = CastView(caster)
      self.setSubmit('Cast')
      self.setClose('Cancel')
      self.setTitle(caster.name)
      self.setView(castView.build())
      
      
  def open(self):
    if not self.view:
      return
    payload = {
      "token": os.environ.get('SECRET'),
      "trigger_id": self.triggerId,
      "state": 'Testing!',
      "view": self.view
    }
    url = 'https://slack.com/api/views.open?{}'.format(urllib.parse.urlencode(payload))
    req = requests.get(url)
    res = req.json()
    self.id = res.get('view').get('id')
    self.hash = res.get('view').get('hash')
    print(res)
  
  def setSubmit(self, text):
    self.header['submit'] = {
      "type": "plain_text",
      "text": text,
      "emoji": True
    }
    return
    
  def setClose(self, text):
    self.header['close'] = { 
      "type":"plain_text",
      "text": text,
      "emoji":True
    }
    return
  
  def setTitle(self, text):
    self.header['title'] = {
      "type":"plain_text",
      "text": text,
      "emoji":True
    }
    return
  
  def setView(self, view):
    self.view = self.header
    self.view['blocks'] = view
    
  
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