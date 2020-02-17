from constant.spells import SPELLS

class spell:
  def __init__(self, type):
    
    if not type in SPELLS:
      return
    
    spell = SPELLS.get(type)
    
    self.cost = spell.cost
    self.duration = spell.duration
    self.cast = spell.cast
    self.type = spell.type
    self.icon = spell.icon
  def getView:
    return {
       "type":"section",
       "text":{ 
          "type":"mrkdwn",
          "text":"*FIREBALL* - 40\n*Inflicts:* Burn\n *Duration*: 5m\n *Cast Time:* Short"
       },
       "accessory":{ 
          "type":"image",
          "image_url":"https://emoji.slack-edge.com/TDBEDSEQZ/burn/297d37e5dadbe697.gif",
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
             "value":"click_me_123"
          }
       ]
    } 