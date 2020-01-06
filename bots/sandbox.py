from bots.bot import Bot
from pymongo import MongoClient
from pprint import pprint
import os

class Sandbox(Bot):
  
  @classmethod
  def description(cls):
    return "`Sandbox` Random Stuff"
  
  def run(self):
    if not self._event.isInChannel('Secret'):
      return
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient(os.environ.get('MONGO'))
    db=client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    pprint(serverStatusResult)
    return
    