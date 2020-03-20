from utils.post import Post
from utils.identity import Identity
from utils.random import Random
from utils.ban import Ban
from utils.channel import Channel
from utils.mongo import Mongo

class Bot(object):
  
  def __init__(self, eventModel, pool, mongoClient = None, user=None):
    self._event = eventModel
    self._postUtil = Post(pool)
    self._identityUtil = Identity()
    self._randomUtil = Random()
    self._banUtil = Ban()
    self._channelUtil = Channel()
    self._mongoUtil = Mongo(mongoClient)
    self._user = user
    
  @classmethod
  def description(cls):
    return ""
  
  def run(self):
    return
  
  def getListView(self):
    return