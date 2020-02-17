from constant.people import IDENTITIES

class Caster:
  def __init__(self, user):
    self.user_id = user
    
    if not user in IDENTITIES:
      return
    
    self.name = IDENTITIES.get(user).get('name')
  
    self.status = 'normal'
    