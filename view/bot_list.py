from view._view import View
import bots


class BotListView(View):
  
  def __init__(self, req):
    self._botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(bots))))

    super().__init__(req)    
  
    
  def build(self):
    
    print(self._botList)
    
    for bot in self._botList:
      self._blocks.append(
        { 
           "type":"section",
           "text":{ 
              "type":"mrkdwn",
              "text":f"*Kin Khao*\n:star::star::star::star: 1638 reviews The sticky rice also goes wonderfully with the caramelized pork belly, which is absolutely"
           },
          "accessory":{ 
            "type":"image",
            "image_url": 'https://emoji.slack-edge.com/TDBEDSEQZ/luffy_dizzy/078316a8f001f0fa.gif',
            "alt_text":"Airstream Suite"
         }
        }
      )
    
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