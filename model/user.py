from pymongo import MongoClient
from pprint import pprint
import os
import json

class User:
  
  def __init__(self, event, db):
    client = MongoClient(os.environ.get('MONGO'))
    db=client.slack
    cursor = db.users.find({"SlackID": event.user()})
    if cursor.count == 0:
      self.createNewProfile(event.user())
    else:
      print (cursor.next())
    
  def createNewProfile(self, id, db):
    newUser = {
      'SlackID':  id
    }
    return
  