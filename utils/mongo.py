from pymongo import MongoClient
import os

class Mongo:
  
  def __init__(self, client):
    self._db = client.slack
    
  def findOne(self, collectionName, query):
    return self._db[collectionName].find_one(query)