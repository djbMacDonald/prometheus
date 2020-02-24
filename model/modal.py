from model.caster import Caster
from view.cast import CastView
from view.bot_list import BotListView
from view._view import View
from view.chaos import ChaosView
from view.chaos_admin import ChaosAdminView
import requests
import os
import json
import urllib
import view

class Modal:
  def __init__(self, type, req, user=None):
    
    botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(view))))
    
    self.triggerId = req.get('trigger_id')
    
    if not self.triggerId:
      return
    
    #Build a Spell Cast ciew
    if type == 'cast':
      self.view = CastView(req).build()
      self.id = 'cast'

    if type == 'bot_list':
      self.view = BotListView(req).build()
      
    if type == 'chaos':
      self.view = ChaosView(req, user).build()
      
    if type == 'chaos_admin':
      self.view = ChaosAdminView(req, user).build()
      
      
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
    return
    self.id = res.get('view').get('id')
    self.hash = res.get('view').get('hash')

def updateModal(id, view):
  if not id or not view:
    return
  payload = {
    "token": os.environ.get('SECRET'),
    'external_id': id,
    "view": view
  }
  url = 'https://slack.com/api/views.update?{}'.format(urllib.parse.urlencode(payload))
  res = requests.get(url)
