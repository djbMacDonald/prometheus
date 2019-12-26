import random
from model.identity import Identity
from constant.people import IMPERSONATIONS

class IdentityUtil:
  
  def getRandomIdentity(self):
    identityRow = random.choice(IMPERSONATIONS)
    return Identity(identityRow.get('username'), identityRow.get('profilePicture'))
  
  def randomImageUrl(self):
    return 'https://robohash.org/{}?set=set{}'.format(random.randint(1,99999), random.randint(1,4))
  
  def pingUser(self, user):
    return '<@' + user + '>'