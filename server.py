from flask import Flask, request, render_template, jsonify, Response
from model.modal import Modal
from multiprocessing import Pool
from constant.channels import CHANNELS
import json
import jsons
from model.slackevent import SlackEvent
import pprint
import traceback
import urllib
import requests
from model.caster import Caster
from model.event import Event
from utils.ban import Ban
from utils.log import Log
import bots
from utils.post import Post
import time
import sched
import os
import asyncio
from model.user import User

app = Flask(__name__)

log = True
handledEvents = []
bans = {}

def _convertCase(name):
  components = name.split('_')
  return''.join(x.title() for x in components)

def _callBot(bot, originalEvent, pool, client, user=None):
  moduleType = getattr(bots, bot)
  className = _convertCase(bot)
  runner = getattr(moduleType, className)(originalEvent, pool, client, user)
  return runner.run()

botList = sorted(list(filter(lambda name: not name.startswith("_"), dir(bots))))

@app.route("/listen", methods=['POST'])
def inbound():
  data = request.get_json(force=True)
  logUtil = Log()
  
  if data.get('event_id') in handledEvents or not data.get('event'):
    return data, 200
  else:
    handledEvents.append(data.get('event_id'))
  
  
  if log:
    cleanData = data.get('event')
    if 'blocks' in cleanData:
      del(cleanData['blocks'])
    print(json.dumps(cleanData, indent=2, sort_keys=True))
    
    
  pool = Pool(1)
  originalEvent = Event(data, bans)
  # client = MongoClient(os.environ.get('MONGO'))
  client = None
  if originalEvent.isAMessage() and not originalEvent.isFromABot():
    user = User(originalEvent)
  else:
    user = None
  for bot in botList:
    try:
      result = _callBot(bot, originalEvent, pool, user)
      if result == 'end':
        return Response(), 200
    except Exception as error:
      pprint.pprint(error)
      print(traceback.format_exc())
    
  if not originalEvent.isFromABot() and originalEvent.isAMessage():
    logUtil.logToFile(originalEvent)
  pool.close()
  pool.join()
  return data, 200

@app.route('/bot', methods=['POST'])
def list():
  req = request.values.to_dict()
  trigger = req.get('trigger_id')
  user = User(Event(req))
  text = request.form.get('text')
  words = text.split()
  if words[0].lower() == 'list':
    
    modal = Modal('bot_list', trigger, user)
    modal.open()
    return Response(), 200
  if words[0].lower() == 'configure':
    return _botConfigure(words[1], words[2], words[3])

def _botConfigure(action, bot, value):
  if action not in ['frequency', 'target']:
    return 'Supported actions are frequency and target'
  if bot not in ['code']:
    return 'Supported bots are code'
  
  # client = MongoClient(os.environ.get('MONGO'))
  # client.slack.bots.update_one({'name': bot}, {'$set': {action: value}})
  return '{} bot {} set to {}'.format(bot, action, value)

@app.route('/push_me', methods=['POST'])
def stuff():
  data = request.form.to_dict(flat=False)
  data = json.loads(data['payload'][0])
  triggerId = data['trigger_id']
  user = data['user']['id']
  
  postData = {
     'user': user, 
     'scopes': 'chat:write:user',
     'trigger_id': triggerId,
     'token': os.environ.get('SECRET')
   }
  url = 'https://www.slack.com/api/apps.permissions.users.request?{}'.format(urllib.parse.urlencode(postData))
  requests.get(url)
  return Response(), 200

@app.route('/mega', methods=['POST'])
def test():
  
  data = request.form.to_dict()
  
  message = getChungus(data.get('text'))
  if message:
    return jsonify(
        response_type='in_channel',
        text=message,
        delete_original=True
    )
  return Response(), 200

@app.route('/mega/<search>', methods=['GET'])
def test2(search):
  
  if search == 'list':
      url = 'https://wayfair.slack.com/api/emoji.adminList?token={}&count=100000'.format(os.environ.get('EMOJI'))
      res = requests.get(url)
      emojis = res.json();
      emojis = emojis.get('emoji')
      gigaEmojis = dict();
      
      for emoji in emojis:
          regex = r"(.+[-_])(\d+)[-_](\d+)$"
          if bool(re.search(regex, emoji.get('name'))):
              matches = re.finditer(regex, emoji.get('name'), re.MULTILINE)
              for matchNum, match in enumerate(matches, start=1):
                  groups = match.groups();
                  if gigaEmojis.get(groups[0]):
                      gigaEmojis.get(groups[0]).append((emoji.get('name'), int(groups[1]), int(groups[2])))
                  else:
                      gigaEmojis[groups[0]] = [(emoji.get('name'), int(groups[1]), int(groups[2]))]
      message = ''
      for key in sorted(gigaEmojis.keys()):
        message = message + key + "<br />"
      return message
    
  else :
    output = getChungus(search)
    if output:
      return "<br />".join(output.split("\n"))
    return Response(), 200
  
@app.route('/ban', methods=['POST'])
def bannedWords():
  global bans
  text = request.form.get('text')
  words = text.split(' ')
  postUtil = Post(Pool(1))
  if text.isdigit():
    getNewBans(int(text), {})
    postUtil.addMessageToChannel(text + ' new bans added', CHANNELS['Underscore'])
    return Response(), 200

  elif len(words) > 1 or not text.isalpha() or text in bans.keys():
    ##call them an idiot
    return Response(), 200
  if text == 'list':
    banUtil = Ban()
    dailybans = banUtil.getBans()

    postUtil.addMessageToChannel('Current Bans: ' + ', '.join(dailybans), CHANNELS['Underscore'])
  elif text == 'clear':
    bans = {}
    saveBans()
    postUtil.addMessageToChannel('Bans Cleared!', CHANNELS['Underscore'])
  else:
    addBan(text)
    saveBans()
    postUtil.addMessageToChannel(text + ' is now banned', CHANNELS['Underscore'])
  return Response(), 200

@app.route('/quicktime', methods=['POST'])
def quicktime():

  event = SlackEvent(json.loads(request.values.get('payload')))

  return {
      "response_action": "update",
      "view": {
        "type": "modal",
        "title": {
          "type": "plain_text",
          "text": "Updated view"
        },
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "plain_text",
              "text": "THIS FUCKIN BUTTON WORKS. HAPPY NOW?!?!?"
            }
          }
        ]
      }
    }
  


def getChungus(searchTerm):
  url = 'https://games-club-external.slack.com/api/emoji.adminList?token={}&queries=["{}"]&count=100000'.format(os.environ.get('MEGA'), searchTerm)
  res = requests.get(url)
  emojis = res.json();
  emojis = emojis.get('emoji')
  gigaEmojis = dict();

  for emoji in emojis:
      regex = r"(.+[-_])(\d+)[-_](\d+)$"
      if bool(re.search(regex, emoji.get('name'))):
          matches = re.finditer(regex, emoji.get('name'), re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
              groups = match.groups();
              if gigaEmojis.get(groups[0]):
                  gigaEmojis.get(groups[0]).append((emoji.get('name'), int(groups[1]), int(groups[2])))
              else:
                  gigaEmojis[groups[0]] = [(emoji.get('name'), int(groups[1]), int(groups[2]))]

  message = ''

  for emoji, value in gigaEmojis.items():
     sortedEmojis = (sorted(value, key=operator.itemgetter(1,2)))
     maxY = 0
    
     prevX = 0
     prevY = 0
     for emoji, x, y in sortedEmojis:
        if x == 0:
          prevX = -1;
        if y == 0:
          prevy = -1
        if int(x) > prevX:
          prevX = int(x);
          if len(message) > 0:
            message = message + '\n'
          prevY = 0
        elif int(y) > (prevY + 1):
          while prevY < (int(y) - 1) and int(y) - prevY < 4:
           message = message + ':blank:'
           prevY = prevY + 1
        message = message + ':{}:'.format(emoji)
        prevY = int(y)
     if len(message) > 0:
      message = message + ' \n'
  return message

def loadBans():
  global bans
  
  expiredBans = [];
  currentTime = int(round(time.time()))
    
  if not bans:
    with open('new_ban_list.json') as data_file:
      bans = json.loads(data_file.read())
  
  
  for ban in bans.keys():
    if bans[ban] < currentTime:
      expiredBans.append(bans.pop(ban))
  
  if not bans:
    bans = getNewBans(NUMBER_OF_WORDS_TO_BAN, expiredBans)
    
def getNewBans(numberOfBans, expiredBans):
  global bans
  newBans = {}
  lines = open('{}_logfile.txt'.format(CHANNELS['Chaos']), 'r').read().splitlines()
  for x in range (0, numberOfBans):
    myline = random.choice(lines)
    myword = '1';
    while not myword.isalpha() or myword in newBans.keys() or myword in expiredBans:
      myline = random.choice(lines)
      myword = random.choice(myline.split(' '))
    addBan(myword)
    saveBans()
    
def saveBans():
  global bans
  f = open('new_ban_list.json', 'w+')
  f.write(json.dumps(bans))
  f.close()
  
def addBan(word):
  global bans
  if word in bans.keys():
    return
  tz = timezone('EST')
  n = datetime.datetime.now(tz)
  bans[word] = int(round(time.time())) + int(round(((24 - n.hour - 2) * 60 * 60) + ((60 - n.minute - 1) * 60) + (60 - n.second)))
  
@app.route('/cast', methods=['POST'])
def cast():
  req = request.values.to_dict()
  user = User(Event(req))
  
  modal = Modal('cast', req.get('trigger_id'), user)
  modal.open()
  return Response(), 200

@app.route('/chaos', methods=['POST'])
def chaos():
  #home for chaos management
  req = request.values.to_dict()
  trigger = req.get('trigger_id')
  user = User(Event(req))

  if not req.get('text'):
    #Manage Personal Chaos Settings
    modal = Modal('chaos', trigger, user)
    modal.open()
  elif req.get('text') == 'admin':
    #Manage Overall Chaos
    modal = Modal('chaos_admin', trigger, user)
    modal.open()
  elif req.get('text') == 'users':
    modal = Modal('user', trigger, user)
    modal.open()
  
  return Response(), 200
  
if __name__ == "__main__":
  app.run()
