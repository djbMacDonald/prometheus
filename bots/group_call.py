from utils.post_util import PostUtil
import random
from identity import Identity
import os
import urllib
import requests
from utils.identity import IdentityUtil
from constants.people import USERS, GROUP_LIST

class GroupCallBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._identityUtil = IdentityUtil()
  
  def run(self):
    if not self._event.isAMessage():
      return
    for group in GROUP_LIST:
      if group in self._event.text().lower():
        pings=''
        for user in GROUP_LIST[group]:
          pings+=self._identityUtil.pingUser(USERS[user])+' '
        print(pings)
        self._postUtil.addMessageToThread(pings, self._event.channel(), self._event.id(), self._identityUtil.getRandomIdentity())