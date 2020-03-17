import view
import sys


class ViewFactory:
  
  def getView(type, user=None):
    sys.path.append('/app/view')
    moduleType = __import__(type, fromlist=[view])
    className = _convertCase(type)
    return getattr(moduleType, className)(user)
  
  
def _convertCase(type):
  final = ''
  words = type.split('_')
  for word in words:
    word = word.capitalize()
    final = final + word
  return f"{final}View"