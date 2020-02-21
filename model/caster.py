import requests
import urllib
import os
import json

from constant.view import DIVIDER

from constant.people import (
  PEOPLE
)
from model.spell import Spell

class Caster:
  def __init__(self, user):
    self.user_id = user
    
    if not user in PEOPLE:
      return
    self.name = PEOPLE.get(user).get('username')
    self.icon = PEOPLE.get(user).get('profilePicture')
  
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
  
