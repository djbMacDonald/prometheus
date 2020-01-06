from utils.post import PostUtil
from utils.identity import IdentityUtil
from utils.random import RandomUtil

class ParentBot(Object):
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
    self._randomUtil = RandomUtil()