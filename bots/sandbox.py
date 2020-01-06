from bots.bot import Bot
from pymongo import MongoClient
from pprint import pprint
import json
import os

class Sandbox(Bot):
  
  # @classmethod
  # def description(cls):
    # return "`Sandbox` Random Stuff"
  
  def run(self):
    if not self._event.isInChannel('Secret'):
      return
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient(os.environ.get('MONGO'))
    db=client.slack
    event = self._event.event()
    if 'blocks' in event:
      del(event['blocks'])
    print(event)

    event['_id'] = event['client_msg_id']
    db.events.insert_one(event)
    
    # Issue the serverStatus command and print the results
    return
    