from pymongo import MongoClient
from pprint import pprint
import os
import json

class User:
  
  def __init__(self, event, db = None):
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
  