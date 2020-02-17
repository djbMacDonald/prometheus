from constant.people import IDENTITIES
from model.spell import Spell

class Caster:
  def __init__(self, user):
    self.user_id = user
    
    if not user in IDENTITIES:
      return
    
    self.name = IDENTITIES.get(user).get('name')
  
    self.status = 'Healthy'
    self.mana = 100
    self.maxMana = 100
    self.cha = 12
    self.int = 12
    self.con = 12
    self.dex = 12
    self.spells = [Spell('fireball'), Spell('confusion')]
    