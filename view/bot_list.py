from view._view import View
import bots


class BotListView(View):
  
  def __init__(self, req):
    super().__init__(req)    
  
    
  def build(self):
    
    self._finalize()
    return self.view
  
  def _botList():
    for bot in sorted(map(_getDescription, botList)):
      print(bot)
                
  
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