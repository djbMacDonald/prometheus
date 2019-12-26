from utils.post import PostUtil
import random
from constant.people import USERS, IDENTITIES

class UnderscoreBot():
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    
  def _runConditition(self):
    return self._event.isInChannel('Underscore') and self._event.isFromChaosUser()
  
  def run(self):
    if not self._runConditition():
      return
    if ' ' in self.text:
      text = self._event.text().replace(' ', '-')
      self._postUtil.deleteMessage(self._event.channel(), self._event.id())
      identity = IDENTITIES[USERS[self._event.user()].lower()]
      self._postUtil.addMessage(text, self._event.channel(), self._event.threadId(), Identity(identity.get('username'), identity.get('profilePicture')))
    return 'end'
