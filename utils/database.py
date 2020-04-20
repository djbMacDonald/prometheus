from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

import hashlib as hl

class Database:
  DB_ENGINE = {
    SQLITE: 'sqlite:///{DB}'
  }
  
  db_engine = None
  def __init__(self, dbtype, username='', password='', dbname=''):
    dbtype = dbtype.lower()
    if dbtype in self.DB_ENGINE.keys():
      engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
      self.db_engine = create_engine(engine_url)
      print(self.db_engine)
    else:
      print("DBType is not found in DB_ENGINE")
      
  def initialize_civ_db(self):
    metadata = Metadata()
    payload_hashes = Table(Payloads, metadata, Column('PayloadHash', Binary, primary_key=True))