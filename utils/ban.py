import random
from model.identity import Identity
import requests
import time
from pytz import timezone
from constant.channels import CHANNELS

class BanUtil:
  
  def banNewWord(self):
    bans = dict();
    lines = open('{}_logfile.txt'.format(CHANNELS['Chaos']), 'r').read().splitlines()
    myline = random.choice(lines)
    myword = '1';
    while not myword.isalpha() or myword in bans.keys():
      myline = random.choice(lines)
      myword = random.choice(myline.split(' '))
    print(myline)
    
    tz = timezone('EST')
    n = datetime.datetime.now(tz)
    expirationDate = int(round(time.time())) + int(round(((24 - n.hour - 2) * 60 * 60) + ((60 - n.minute - 1) * 60) + (60 - n.second)))
    newBan = '{}~~~{}'.format(myword, expirationDate)
    f = open('banlist.txt', 'w+')
    f.write(newBan)
    f.close()
    print(newBan)
    bans['myword'] = expirationDate
    return bans;
  
  def getBans(self):
    bans = dict()
    lines = open('banlist.txt', 'r').read().splitlines()
    if len(lines) < 1 or len(lines[0]) < 1:
      return bans
    
    for line in lines:
      ban = line.split('~~~');
      bans[ban[0]] = ban[1]
    return bans;

def activeBans(self, bans):
    for ban in bans.items():
      if (int(ban[1]) < int(round(time.time()))):
        del bans[ban[0]]
    return bans