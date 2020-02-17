from constant.people import IDENTITIES
from model.spell import Spell

class Caster:
  def __init__(self, user):
    self.user_id = user
    
    if not user in IDENTITIES:
      return
    
    self.name = IDENTITIES.get(user).get('name')
  
    self.status = 'Healthy'
    self.mana = 100
    self.maxMana = 100
    self.cha = 12
    self.int = 12
    self.con = 12
    self.dex = 12
    self.spells = [Spell('fireball'), Spell('confusion')]
    
    
  def getView(self):
    
    view = getHeader()
  
    blocks = [];
    blocks.append(self.getStatus())
    
  def getStatus(self):
    return { 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":"*Status:* {self.status}\n*Mana:* 100/100\n *CHA:* 12 *INT:* 12\n*CON:* 12 *DEX:* 12"
         },
         "accessory":{ 
            "type":"image",
            "image_url":"https://ca.slack-edge.com/TDBEDSEQZ-UDDE5960N-9141f5699aec-48",
            "alt_text":"Airstream Suite"
         }
    }
    blocks = [
      ,
      { 
         "type":"divider"
      },
      { 
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
            "options":[ 
               { 
                  "text":{ 
                     "type":"plain_text",
                     "text":"Drew",
                     "emoji":True
                  },
                  "value":"drew"
               },
               { 
                  "text":{ 
                     "type":"plain_text",
                     "text":"Dakota",
                     "emoji":True
                  },
                  "value":"dakota"
               },
               { 
                  "text":{ 
                     "type":"plain_text",
                     "text":"Brenden",
                     "emoji":True
                  },
                  "value":"brenden"
               },
               { 
                  "text":{ 
                     "type":"plain_text",
                     "text":"Mei",
                     "emoji":True
                  },
                  "value":"mei"
               },
               { 
                  "text":{ 
                     "type":"plain_text",
                     "text":"Victoria",
                     "emoji":True
                  },
                  "value":"victoria"
               }
            ]
         }
      },
      { 
         "type":"divider"
      },
      { 
         "type":"divider"
      },
      { 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":"*Confusion* - 20\n*Inflicts:* Confusion\n *Duration*: 1m\n *Cast Time:* Instant"
         },
         "accessory":{ 
            "type":"image",
            "image_url":"https://emoji.slack-edge.com/TDBEDSEQZ/luffy_dizzy/078316a8f001f0fa.gif",
            "alt_text":"Airstream Suite"
         }
      },
      { 
         "type":"actions",
         "elements":[ 
            { 
               "type":"button",
               "style": "danger",
               "text":{ 
                  "type":"plain_text",
                  "text":"Selected",
                  "emoji":True
               },
               "value":"click_me_123"
            }
         ]
      },
      { 
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
       ]
  
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
          
            
    