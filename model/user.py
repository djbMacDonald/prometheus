from pymongo import MongoClient
from model._model import BaseModel
import requests
from pprint import pprint
import os
import urllib


import json

class User(BaseModel):
  
  def __init__(self, event, db = None):
    self._event = event
    client = MongoClient(os.environ.get('MONGO'))
    self._db = db
    if not self._db:
      self._db=client.slack
    cursor = self._db.users.find({"id": event.user()})
    if cursor.count() == 0:
      self.createNewProfile(event.user(), db)
      self.__init__(event, db)
    else:
      print (cursor[0])
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
  
  def isAWizard(self):
    return hasattr(self, 'wizard') and self.wizard == True