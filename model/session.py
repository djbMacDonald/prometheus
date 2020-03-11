import json

from model.event import Event
from model.user import User
from multiprocessing import Pool


class Session:
  
  def __init__(self, data):
    
    self._event = Event(data, bans)
    
    if self._event.isAMessage() and not self_event.isFromABot():
      self._user = User(self._event)
    else:
      self._user = None
      
    self._pool = Pool(1)
    
    return
  
  def logCleanEvent(self):
    cleanData = data.get('event')
    if 'blocks' in cleanData:
      del(cleanData['blocks'])
    print(json.dumps(cleanData, indent=2, sort_keys=True))