import random
from model.identity import Identity as IdentityModel
from constant.people import IMPERSONATIONS

# move to static functions
class Identity:
  
  def getRandomIdentity(self):
    identityRow = random.choice(IMPERSONATIONS)
    return IdentityModel(identityRow.get('username'), identityRow.get('profilePicture'))
  
  def randomImageUrl(self):
    return 'https://robohash.org/{}?set=set{}'.format(random.randint(1,99999), random.randint(1,4))
  
  def pingUser(self, user):
    return '<@' + user + '>'