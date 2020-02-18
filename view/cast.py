from constant.view import DIVIDER

from constant.people import (
  IDENTITIES,
  CHAOS_USERS
)

class CastView:
  
  def __init__(self, caster):
    self.caster = caster
    if not self.caster:
      return
    
    self._blocks=[]
  
  def buildStatus(self):
    self._blocks.append({ 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":f"*Status:* {self.caster.status}\n*Mana:* {self.caster.mana}/{self.caster.maxMana} *CHA:* {self.caster.cha} *INT:* {self.caster.int}\n*CON:* {self.caster.con} *DEX:* {self.caster.dex}"
         },
         "accessory":{ 
            "type":"image",
            "image_url":self.caster.icon,
            "alt_text":"Airstream Suite"
         }
    })
    self._blocks.append(DIVIDER)
  
  def buildTargets(self):
    options = []
    
    for user, id in CHAOS_USERS.items():
      if self.caster.user_id == id:
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
    
    self._blocks.append({ 
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
    self._blocks.append(DIVIDER)
    
  def buildSpells(self):
    for spell in self.caster.spells:
      description, action = spell.getView()
      self._blocks.append(description)
      self._blocks.append(action)
      
  def build(self):
    self.buildStatus()
    self.buildTargets()
    self.buildSpells()
    return self._blocks
  
  