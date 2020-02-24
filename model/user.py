from pymongo import MongoClient
import requests
from pprint import pprint
import os
import urllib


import json

class User:
  
  def __init__(self, event, db = None):
    self._event = event
    print('here!!!!!')
    client = MongoClient(os.environ.get('MONGO'))
    if not db:
      db=client.slack
    cursor = db.users.find({"id": event.user()})
    if cursor.count() == 0:
      self.createNewProfile(event.user(), db)
    else:
      print (cursor[0])
    
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