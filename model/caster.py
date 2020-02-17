import requests
import urllib
import os
import json

from constant.view import DIVIDER

from constant.people import (
  IDENTITIES,
  CHAOS_USERS
)
from model.spell import Spell

class Caster:
  def __init__(self, user):
    self.user_id = user
    
    if not user in IDENTITIES:
      return
    
    self.name = IDENTITIES.get(user).get('username')
    self.icon = IDENTITIES.get(user).get('profilePicture')
  
    self.status = 'Healthy'
    self.mana = 100
    self.maxMana = 100
    self.cha = 12
    self.int = 12
    self.con = 12
    self.dex = 12
    self.spells = [Spell('fireball'), Spell('confusion')]
    
    self.viewBlocks = []
    
    
    
  def openView(self, trigger_id):
    payload = {
      "token": os.environ.get('SECRET'),
      "trigger_id": trigger_id,
      "state": 'Testing!',
      "view": self.getView()
    }
    url = 'https://slack.com/api/views.open?{}'.format(urllib.parse.urlencode(payload))
    res = requests.get(url)
    print(res.json())
    
  def getView(self):
    view = self.getHeader()
    self.buildStatus()
    self.buildTargets()
    self.buildSpells()
    view['blocks'] = self.viewBlocks
    print(json.dumps(view))
    return view

      
  
  def getHeader(self):
    return { 
       "type":"modal",
       "title":{ 
          "type":"plain_text",
          "text":f"{self.name}",
          "emoji":True
       },
       "submit": {
          "type": "plain_text",
          "text": "Cast",
          "emoji": True
       },
       "close":{ 
          "type":"plain_text",
          "text":"Cancel",
          "emoji":True
       },
    }
  
  def buildStatus(self):
    self.viewBlocks.append({ 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":f"*Status:* {self.status}\n*Mana:* {self.mana}/{self.maxMana} *CHA:* {self.cha} *INT:* {self.int}\n*CON:* {self.con} *DEX:* {self.dex}"
         },
         "accessory":{ 
            "type":"image",
            "image_url":self.icon,
            "alt_text":"Airstream Suite"
         }
    })
    self.viewBlocks.append(DIVIDER)
  
  def buildTargets(self):
    options = []
    
    for user, id in CHAOS_USERS.items():
      if self.user_id == id:
        continue
      options.append(
        { 
            "text":{ 
               "type":"plain_text",
               "text":user.capitalize(),
               "emoji":True
            },
            "value":user
         }
      )
    
    self.viewBlocks.append({ 
         "type":"input",
         "label":{ 
            "type":"plain_text",
            "text":"Select a Target",
            "emoji":True
         },
         "element":{ 
            "type":"static_select",
            "placeholder":{ 
               "type":"plain_text",
               "text":"Select an item",
               "emoji":True
            },
            "options": options
         }
      })
    self.viewBlocks.append(DIVIDER)
    
  def buildSpells(self):
    for spell in self.spells:
      description, action = spell.getView()
      self.viewBlocks.append(description)
      self.viewBlocks.append(action)