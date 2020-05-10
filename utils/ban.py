import random
from model.identity import Identity
import requests
import time
from pytz import timezone
from constant.bans import BAN_BAN_LIST
import datetime
from constant.channels import chaosChannel

# move to static functions
class Ban:
  
  def banNewWord(self):
    bans = dict();
    lines = open('{}_logfile.txt'.format(chaosChannel()), 'r').read().splitlines()
    myline = random.choice(lines)
    myword = '1';
    while not myword.isalpha() or myword in bans.keys() or myword.lower() in BAN_BAN_LIST:
      myline = random.choice(lines)
      myword = random.choice(myline.split(' '))
    todayDate = datetime.date.today()
    newBan = '{}~~~{}'.format(myword, todayDate)
    f = open('banlist.txt', 'w+')
    f.write(newBan)
    f.close()
    bans['myword'] = todayDate
    return bans;
  
  def banWord(self, word):
    todayDate = datetime.date.today()
    newBan = '{}~~~{}'.format(word, todayDate)
    f = open('banlist.txt', 'w+')
    f.write(newBan)
    f.close()
    bans['myword'] = todayDate
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
    copy = bans.copy()
    todayDate = datetime.date.today()
    
    for ban in bans.items():
      banDate = datetime.datetime.strptime(ban[1], '%Y-%m-%d').date()
      if banDate < todayDate:
        del copy[ban[0]]
    return copy
