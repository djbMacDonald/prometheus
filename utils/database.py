from sqlalchemy import create_engine, Table, Column, Binary, MetaData

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
    payloads = Table(Payloads, metadata, Column('PayloadHash', Binary, primary_key=True))
    try:
      metadata.create_all(self.db_engine)
    except Exception as e:
      print("Error occurred during table creation.")
      print(e)