from utils.post import PostUtil
from utils.identity import IdentityUtil
from utils.random import RandomUtil
from utils.ban import BanUtil

class Bot(object):
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
    self._randomUtil = RandomUtil()
    self._banUtil = BanUtil()