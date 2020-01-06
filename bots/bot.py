from utils.post import Post
from utils.identity import Identity
from utils.random import Random
from utils.ban import Ban

class Bot(object):
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = Post(pool)
    self._identityUtil = Identity()
    self._randomUtil = Random()
    self._banUtil = Ban()
    
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    return