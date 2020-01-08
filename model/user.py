from pymongo import MongoClient
from pprint import pprint
import json

class User:
  
  def __init__(event):
    client = MongoClient(os.environ.get('MONGO'))
    db=client.slack
    result = db.users.find({"SlackID": event.user()}).limit(1)
    print(result)
  