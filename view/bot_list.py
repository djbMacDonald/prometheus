from view._view import View
from constant.view import DIVIDER
import bots


class BotListView(View):
  
  def __init__(self, req):
    self._botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(bots))))

    super().__init__(req)    
  
    
  def build(self):
    
    print(self._botList)
    
    for bot in self._botList:
      description = _getDescription(bot)
      if not description:
        continue
      text = f"*{_convertCase(bot)}*\n>{description}"
      print (text)
      self._blocks.append(
        { 
           "type":"section",
           "text":{ 
              "type":"mrkdwn",
              "text": text
           }
        }
        
      )
      self._blocks.append({
         "type":"actions",
         "elements":[ 
            { 
               "type":"button",
               "style": "primary" 'danger',
               "text":{ 
                  "type":"plain_text",
                  "text":"Choose" ,
                  "emoji":True
               },
               "value":bot
            }
       ]
    })
    
    self._finalize()
    print(self.view)
    return self.view
   
  
def _getDescription(bot):
  try:
    return _getBotAttr(bot, "description")
  except Exception as error:
    pprint.pprint(error)
    print(traceback.format_exc())
    return ""

def _getBotAttr(bot, attrName):
  moduleType = getattr(bots, bot)
  className = _convertCase(bot)
  classType = getattr(moduleType, className)
  return getattr(classType, attrName)()

def _convertCase(name):
  components = name.split('_')
  return''.join(x.title() for x in components)