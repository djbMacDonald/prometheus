from pymongo import MongoClient
from model._model import BaseModel
import requests
from pprint import pprint
import os
import urllib


import json

class User(BaseModel):
  
  def __init__(self, event=None, db = None, user=None):
    self._event = event
    if event:
      user = event.user()
    client = MongoClient(os.environ.get('MONGO'))
    self._db = db
    if not self._db or self._db == None:
      self._db=client.slack
    cursor = self._db.users.find({"id": user})
    if cursor.count() == 0:
      self.createNewProfile(event.user(), self._db)
      self.__init__(event, db)
    else:
      self.populate(cursor[0])
    
  def createNewProfile(self, id, db):
    newUser = self.getUserInfo(id)
    db.users.insert_one(newUser)
    return
  
  def getTrigger(self, user):
    return self._event._trigger_id
  
  def getUserInfo(self, user):
    url = 'https://slack.com/api/users.info'
    payload = {
      'token': os.environ.get('SECRET'),
      'user': user
    }
    res = requests.get(f"{url}?{urllib.parse.urlencode(payload)}")
    return res.json().get('user')
      
  def getDisplayName(self):
    return self.profile.get('display_name')
  
  def getProfilePicture(self):
    return self.profile.get('image_72')
  
  def isWizard(self):
    return hasattr(self, 'wizard') and self.wizard == True
  
  def notifyOnThreads(self):
    return hasattr(self, 'threads') and self.threads == True
  
  def hasDoppleganger(self):
    return hasattr(self, 'doppleganger') and self.doppleganger == True
  
  def update(self, ts):
    if not hasattr(self, 'last_action') or ts > self.last_action:
      db = self._db
      delattr(self, '_db')
      db.users.replace_one({'id': self.id}, self.__dict__)
      setattr(self, '_db', db)
      