class Identity:
  
  def __init__(self, userName = None, profilePicture = None, emoji = None):
    self._userName = userName
    self._profilePicture = profilePicture
    self._emoji = emoji
    
  def userName(self):
    return self._userName
  
  def profilePicture(self):
    return self._profilePicture
  
  def emoji(self):
    if self._emoji and self._emoji[0] == ':' and self._emoji[-1] == ':':
      return self._emoji
    return ":{}:".format(self._emoji)