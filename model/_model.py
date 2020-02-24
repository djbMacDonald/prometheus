class BaseModel:
  
  def populate(self, data):
    for key in data.keys():
      setattr(self, key, data[key])    