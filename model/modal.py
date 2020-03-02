import requests
import importlib
import os
import json
import urllib
from utils.view_factory import ViewFactory

class Modal:
  def __init__(self, type, trigger_id, user):
        
    if not user:
      return
        
    self.triggerId = trigger_id
    
    if not self.triggerId:
      return
    
    self.view = ViewFactory.getView(type, user).build()
    
      
  def open(self):
    if not self.view:
      return
    payload = {
      "token": os.environ.get('SECRET'),
      "trigger_id": self.triggerId,
      "view": self.view
    }
  
    url = 'https://slack.com/api/views.open'
    headers = {'content-type': 'application/json; charset=utf-8', "Authorization": f"Bearer {os.environ.get('SECRET')}"}
    req = requests.post(url, json.dumps(payload), headers=headers)
    res = req.json()
    print(json.dumps(payload))
    print (res)
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