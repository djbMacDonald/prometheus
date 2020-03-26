from bots._bot import Bot
from pymongo import MongoClient
from model.user import User
from pprint import pprint
import json
import os

class Sandbox(Bot):
  
  _active = False
  
  # @classmethod
  # def description(cls):
    # return "`Sandbox` Random Stuff"
  
  def run(self):
    # if not self._event.isInChannel('Megamoji'):
    #   return
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    # client = MongoClient(os.environ.get('MONGO'))
    # db=client.slack
    # event = self._event.event()
    # if 'blocks' in event:
    #   del(event['blocks'])
    # event['_id'] = event['client_msg_id']
    # print(event)
    
    # db.events.insert_one(event)
    
    # messages = db.events.find({"channel": "CDU145F08"})
    # for m in messages:
      # print(m)
    
    # Issue the serverStatus command and print the results
    return
    if not self._event.isFromABot():
      user = User(self._event)
    return
    