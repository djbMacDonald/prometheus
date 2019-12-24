class Identity:
  
  def __init__(self, userName = None, profilePicture = None):
    self._userName = userName
    self._profilePicture = profilePicture
    
  def userName(self):
    return self._userName
  
  def profilePicture(self):
    return self._profilePicture