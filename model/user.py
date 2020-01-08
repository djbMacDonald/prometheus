from pymongo import MongoClient
from pprint import pprint
import os
import json

class User:
  
  def __init__(self, event):
    client = MongoClient(os.environ.get('MONGO'))
    db=client.slack
    print(db.users.find({"SlackID": event.user()}).count())
  