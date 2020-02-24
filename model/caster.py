import requests
import urllib
import os
import json
from model._model import BaseModel

from constant.view import DIVIDER

from constant.people import (
  PEOPLE
)
from model.spell import Spell

class Caster(BaseModel):
  def __init__(self, user):
    self._user = user
    self.user_id = user.id
    self.name = user.getDisplayName()
    self.icon = user.getProfilePicture()
    self.loadStatus()
    self.status = 'Healthy'
    self.mana = 100
    self.maxMana = 100
    self.cha = 12
    self.int = 12
    self.con = 12
    self.dex = 12
    self.spells = [Spell('fireball'), Spell('confusion')]
    
    
  def getSelectedSpell(self):
    for spell in self.spells:
      if spell.selected:
        return spell.name
  
  def loadStatus(self):
    self._user._db.casters.put_one({
      'id': self._user.id,
      'status': 'Healthy',
      'mana': 100,
      'cha': 12,
      'int': 12,
      'con': 12,
      'dex': 12,
      'spells': ','.join(['fireball', 'confusion'])
    })
    cursor = self._user._db.casters.find_one({'id': self._user.id});
    if not cursor or cursor.count() == 0:
      self.status = 'Muggle'
      print('Muggle')
      return
    else:
      print (cursor[0])
      self.populate(cursor[0])  
  

  