from constant.people import USERS, IDENTITIES
from constant.channels import CHANNELS

class Event:
  
  def __init__(self, data, bans):
    self._event = data.get('event')
    self._data = data
    self._bans = bans
    
    self._type = self._event.get('type') 
    self._user = self._event.get('user')
    self._threadId = self._event.get('thread_ts')
    self._text = self._event.get('text')
    self._botId = self._event.get('bot_id')
    self._subType = self._event.get('subtype')
    self._hidden = self._event.get('hidden')
    self._bans = bans
    self._reaction = self._event.get('reaction')
    
    if self._type == 'reaction_added':
      self._channel = self._event.get('item').get('channel')
      self._id = self._event.get('item').get('ts')
    else :
      self._channel = self._event.get('channel')
      self._id = self._event.get('ts')
      
  def event(self):
    return self._event
  
  def data(self):
    return self._data
  
  def bans(self):
    return self._bans
  
  def type(self):
    return self._type
  
  def user(self):
    return self._user
  
  def threadId(self):
    return self._threadId
  
  def text(self):
    return self._text
  
  def botId(self):
    return self._botId
  
  def subType(self):
    return self._subType
  
  def hidden(self):
    return self._hidden
  
  def bans(self):
    return self._bans
  
  def reaction(self):
    return self._reaction
  
  def channel(self):
    return self._channel
  
  def id(self):
    return self._id
  
  def isFromABot(self):
    return not not self._botId or self._hidden
  
  def isFromBot(self, name):
    if self._botId == name:
      return self._botId
    return None
  
  def isPartOfAThread(self):
    return not not self._threadId
  
  def isInChannel(self, name):
    if name in CHANNELS:
      return CHANNELS[name] == self._channel
    return None
  
  def isFromChaosUser(self):
    return self._user in IDENTITIES.keys()
  
  def isAMessage(self):
    return self._type == 'message' and not self._subType and not self._hidden
  
  def isFrom(self, name):
    if name.lower() in USERS.keys():
      return USERS[name.lower()] == self.user
    return None