from constant.spells import SPELLS

class Spell:
  def __init__(self, type):
    
    if not type in SPELLS:
      return
    
    spell = SPELLS.get(type)
    
    self.cost = spell.cost
    self.duration = spell.duration
    self.cast = spell.cast
    self.name = spell.name
    self.icon = spell.icon
    self.effect = spell.effect
    self.selected = True if self.name == ''
    
  def getView(self):
    return {
       "type":"section",
       "text":{ 
          "type":"mrkdwn",
          "text":f"*{self.name.upper}* - {self.cost}\n*Inflicts:* {self.effect}\n *Duration*: {self.duration} messages\n *Cast Time:* {'Instant' if self.cast == 0 else '{} Seconds'.format(self.cast)}"
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
             "text":{ 
                "type":"plain_text",
                "text":"Choose",
                "emoji":True
             },
             "value":self.name
          }
       ]
    }