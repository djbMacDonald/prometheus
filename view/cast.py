from constant.view import DIVIDER
from model.caster import Caster
from view._view import View
from constant.people import (
  IDENTITIES,
  CHAOS_USERS
)

class CastView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.caster = Caster(self.user)
    self.external_id = 'cast'
    
  def build(self):
    self.setClose('Cancel')
    self.setTitle(self.caster.name)
    
    self._buildStatus()
    if not self.caster.status == 'Muggle':
      self.setSubmit('Cast')
      self._buildTargets()
      self._buildSpells()
      self.private_metadata = self.caster.getSelectedSpell()
    elif self.user.isAWizard():
      self.setSubmit('Become a Wizard!')
    self._finalize()
    return self.view
  
  
  def _buildStatus(self):
    self._blocks.append({ 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":f"*Status:* {self.caster.status}\n*Mana:* {self.caster.mana}/100\n *CHA:* {self.caster.cha} *INT:* {self.caster.int}\n*CON:* {self.caster.con} *DEX:* {self.caster.dex}"
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
         "block_id": 'cast_targets',
         "label":{ 
            "type":"plain_text",
            "text":"Select a Target",
            "emoji":True
         },
         "element":{          
            "action_id": 'selected_cast_target',
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
  
  def handleAction(self, actions):
    action = actions[0].get('value')
    for spell in self.caster.spells:
      if action == spell.name:
        spell.selected = True
      else:
        spell.selected = False
      