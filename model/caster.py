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
    
  def getSelectedSpell(self):
    for spell in self.spells:
      if spell.selected:
        return spell.name
  
  def loadStatus(self):
    cursor = self._user._db.casters.find({'id': self._user.id})
    if not cursor or cursor.count() == 0:
      self.status = 'Muggle'
      print('Muggle')
      return
    else:
      print (cursor[0])
      self.populate(cursor[0])
      
      setattr(self, 'spells', map(lambda x, ','.split(self.spells)))
  

  