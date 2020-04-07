from view._view import View
from constant.view import DIVIDER
import bots
from pprint import pprint


class BotListView(View):
  
  def __init__(self, user):
    self._botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(bots))))
    super().__init__(user)    
  
    
  def build(self):
    
    self.setTitle('Bot List')    
    self._buildBotList()
    self._finalize()
    return self.view
  
  def _buildBotList(self):
     for bot in self._botList:
      description = _getDescription(bot)
      if not description:
        continue
      text = f"*{_convertCase(bot)}*\n>{description}"
      # print (text)
      self._blocks.append(
        { 
           "type":"section",
           "text":{ 
              "type":"mrkdwn",
              "text": text
           }
        }
      )
      
      # self._blocks.append({
      #    "type":"actions",
      #    "elements":[ 
      #       { 
      #          "type":"button",
      #          "style": 'primary',
      #          "text":{ 
      #             "type":"plain_text",
      #             "text":"Configure" ,
      #             "emoji":True
      #          },
      #          "value":bot
      #       },
      #      { 
      #          "type":"button",
      #          "style": 'danger',
      #          "text":{ 
      #             "type":"plain_text",
      #             "text":"Disable" ,
      #             "emoji":True
      #          },
      #          "value":bot
      #       }
      #    ]
      # })
   
  
def _getDescription(bot):
  try:
    return _getBotAttr(bot, "formatDescription")
  except Exception as error:
    pprint(error)
    # print(traceback.format_exc())
    return ""

def _getBotAttr(bot, attrName):
  moduleType = getattr(bots, bot)
  className = _convertCase(bot)
  classType = getattr(moduleType, className)
  return getattr(classType, attrName)()

def _convertCase(name):
  components = name.split('_')
  return ''.join(x.title() for x in components)

