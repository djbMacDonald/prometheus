import random
from model.identity import Identity
from constant.people import USERS, GROUP_LIST
from bots._bot import Bot

class GroupCall(Bot):
  
  @classmethod
  def description(cls):
    return "`Group Call` Pings all users in a given group. Available are: {}".format(", ".join(GROUP_LIST.keys()))
  
  def run(self):
    if not self._event.isAMessage():
      return
    for group in GROUP_LIST:
      if group in self._event.text().lower():
        pings=''
        for user in GROUP_LIST[group]:
          pings+=self._identityUtil.pingUser(USERS[user])+' '
        self._postUtil.addMessageToThread(pings, self._event.channel(), self._event.id(), self._identityUtil.getRandomIdentity())