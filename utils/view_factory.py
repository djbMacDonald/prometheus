import view
import view.profile

class ViewFactory:
  
  def getView(type, user=None):
    moduleType = getattr(view, type)
    className = _convertCase(type)
    return getattr(moduleType, className)(user)
  
  
def _convertCase(type):
  final = ''
  words = type.split('_')
  for word in words:
    word = word.capitalize()
    final = final + word
  return f"{final}View"