from model.caster import Caster
from view.cast import CastView
import requests
import os
import urllib

class Modal:
  def __init__(self, type, req):
    
    self.triggerId = req.get('trigger_id')
    self.header = {"type": "modal"}
    
    if not self.triggerId:
      return
    
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
    res = requests.get(url)
    print(res.json())
  
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