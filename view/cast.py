from constant.view import DIVIDER
from view._view import View
from constant.people import (
  IDENTITIES,
  CHAOS_USERS
)

class CastView(View):
  
  def __init__(self, caster):
    self.caster = caster
    self._blocks = []
    if not self.caster:
      return
    
  def build(self):
    self._buildStatus()
    self._buildTargets()
    self._buildSpells()
    return self._blocks
  
  def _buildStatus(self):
    self._blocks.append({ 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":f"*Status:* {self.caster.status}\n*Mana:* {self.caster.mana}/{self.caster.maxMana}\n *CHA:* {self.caster.cha} *INT:* {self.caster.int}\n*CON:* {self.caster.con} *DEX:* {self.caster.dex}"
         },
         "accessory":{ 
            "type":"image",
            "image_url":self.caster.icon,
            "alt_text":"Airstream Suite"
         }
    })
    self._blocks.append(DIVIDER)
  
  def _buildTargets(self):
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
    
  def _buildSpells(self):
    for spell in self.caster.spells:
      description, action = spell.getView()
      self._blocks.append(description)
      self._blocks.append(action)
  
  