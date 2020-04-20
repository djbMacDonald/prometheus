from sqlalchemy import create_engine, Table, Column, Binary, MetaData
from sqlalchemy.dialects.sqlite import *

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
    else:
      print("DBType is not found in DB_ENGINE")
      
  def execute_query(self, query=''):
    if query == '': return
    with self.db_engine.connect() as connection:
      try:
        return connection.execute(query)
      except Exception as e:
        print(e)
  
  def does_table_exist(self, table_name = ''):
    if table_name = '': return False
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='{TN}';"
    if self.execute_query(sql.format(TN=table_name)).count() == 0:
      return False
    else:
      return True
    
  def initialize_civ_db(self):
    if self.does_table_exist('Payloads'): return
    metadata = Metadata()
    payloads = Table('Payloads', metadata, Column('PayloadHash', Binary, primary_key=True))
    try:
      metadata.create_all(self.db_engine)
    except Exception as e:
      print("Error occurred during table creation.")
      print(e)
      
  def is_new_civ_payload(self, payload):
    self.initialize_civ_db()
    hl.md5(payload.encode('utf-8')).hexdigest()
    sql = 'INSERT INTO Payloads(PayloadHash) VALUES (?)'
    with self.db_engine.connect() as connection:
      connection.execute(sql, )
    ## WIP, got distracted