from constant.spells import SPELLS

class Spell:
  def __init__(self, type):
    print(type)
    if not type in SPELLS:
      return
    
    spell = SPELLS.get(type)
    
    self.cost = spell.get('cost')
    self.duration = spell.get('duration')
    self.cast = spell.get('cast')
    self.name = spell.get('name')
    self.icon = spell.get('icon')
    self.effect = spell.get('effect')
    self.selected = True if self.name.lower() == 'fireball' else False
    
  def getView(self):
    return ({
       "type":"section",
       "text":{ 
          "type":"mrkdwn",
          "text":f"*{self.name.upper()}* - {self.cost}\n*Inflicts:* {self.effect}\n *Duration*: {self.duration} messages\n *Cast Time:* {'Instant' if self.cast == 0 else '{} Seconds'.format(self.cast)}"
       },
       "accessory":{ 
          "type":"image",
          "image_url": self.icon,
          "alt_text":"Airstream Suite"
       }
    },
    {
       "type":"actions",
       "elements":[ 
          { 
             "type":"button",
             "style": "primary" if self.selected else 'danger',
             "text":{ 
                "type":"plain_text",
                "text":"Choose" if not self.selected else "Selected",
                "emoji":True
             },
             "value":self.name
          }
       ]
    })