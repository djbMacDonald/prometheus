i
def getView(type):
  moduleType = getattr(view, type)
    className = _convertCase(type)
    self.view = getattr(moduleType, className)(user).build()