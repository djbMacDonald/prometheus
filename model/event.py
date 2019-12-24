import constants.channels

class Event:
  
  def __init__(self, data):
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
      
    if self._text and len(self._text) > 0: 
      self._text = self._text.encode('utf-8')
      
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
  
  def isPartOfAThread(self):
    return not not self._threadId
  
  def isInChannel(self, name):
    if name in event_constants.CHANNELS:
      return event_constants.CHANNELS[name] == self.channel
    return None
  
  def isFromChaosUser(self):
    return self._user in event_constants.IDENTITIES.keys()
  
  def isAMessage(self):
    return self._type == 'message' and not self._subType and not self._hidden
  
  def isFrom(self, name):
    if name.lower() in event_constants.USERS.keys():
      return event_constants.USERS[name.lower()] == self.user
    return None