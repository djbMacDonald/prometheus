from pymongo import MongoClient
import requests
from pprint import pprint
import os
import urllib


import json

class User:
  
  def __init__(self, event, db = None):
    self._event = event
    self.getUserInfo(event.user())
    return
    client = MongoClient(os.environ.get('MONGO'))
    if not db:
      db=client.slack
    cursor = db.users.find({"SlackID": event.user()})
    if cursor.count() == 0:
      self.createNewProfile(event.user(), db)
    else:
      print (cursor[0])
    
  def createNewProfile(self, id, db):
    
    newUser = {
      'SlackID':  id
    }
    db.users.insert_one(newUser)
    return
  
  
  def getTrigger(self, user):
    return self._event._trigger_id
  
  def getUserInfo(self):
    url = 'https://slack.com/api/users.info'
    payload = {
      'token': os.environ.get('MONGO'),
      'user': user
    }
    res = requests.get(f"{url}?{urllib.parse.urlencode(payload)}")
    print(res.json())