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
      
  def execute_query(self, query=''):
    if query == '': return
    with self.db_engine.connect() as connection:
      try:
        return connection.execute(query)
      except Exception as e:
        print(e)
  
  def does_table_exist(self, table_name = ''):
    if table_name = '': return False
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';"
    if self.execute_query(sql.format(table_name)).count() == 0:
      