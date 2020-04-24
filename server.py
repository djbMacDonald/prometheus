from flask import Flask, request, jsonify, Response
from model.modal import Modal
# TODO: channels should be in util functions
import constant.channels as ch
import json
# TODO: can slackEvent be combined with event model? Or maybe event model needs a better name
from model.slackevent import SlackEvent
# TODO this should only be in actionQueue
import requests
from model.event import Event
from utils.ban import Ban
from utils.log import Log
import time
# remove for action queue pattern  
import os
from model.user import User
# todo remove wildcard
from utils.server import *
from constant.emotes import DEFAULT_EMOTES
from model.action_queue import ActionQueue
# todo move to bot functions
from model.identity import Identity
# move to a bot somewhere
from constant.people import STEAM

# If you need to define a utility function for this file, do it in utils/server.py
app = Flask(__name__)

handledEvents = []
bans = {}

emotes = getAllEmotes() + DEFAULT_EMOTES;

@app.route("/listen", methods=['POST'])
def inbound():
  mongoClient = None
  user = None
  logUtil = Log()
  data = request.get_json(force=True)
  originalEvent = Event(data, bans)
  actionQueue = ActionQueue(event = originalEvent)
  if data.get('event_id') in handledEvents or not data.get('event'):
    return data, 200
  if originalEvent.isAMessage() and not originalEvent.isFromABot():
    user = User(originalEvent)
  if not originalEvent.isFromABot() and originalEvent.isAMessage():
    logUtil.logToFile(originalEvent)
  
  handledEvents.append(data.get('event_id'))
  
  callAllBots(originalEvent, mongoClient, user, emotes, actionQueue)
  actionQueue.flush()
  
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
    return botConfigure(words[1], words[2], words[3])
  
@app.route('/event_history', methods=['POST'])
def eventHistory():
  req = request.values.to_dict()
  trigger = req.get('trigger_id')
  user = User(Event(req))
  modal = Modal('event_history', trigger, user)
  modal.open()
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
  actionQueue = ActionQueue()
  if len(words) > 1 or not text.isalpha() or text in bans.keys():
    return Response(), 200
  if text.isdigit():
    getNewBans(int(text), {})
    queue.addReply('/ban', underscoreChannel(), None, "{} new bans added".format(text))
  elif text == 'list':
    banUtil = Ban()
    dailybans = banUtil.getBans()
    queue.addReply('/ban', underscoreChannel(), None, "Current Bans: {}".format(', '.join(dailybans)))
  elif text == 'clear':
    bans = {}
    saveBans()
    queue.addReply('/ban', underscoreChannel(), None, "Bans Cleared!")
  else:
    addBan(text)
    saveBans()
    queue.addReply('/ban', underscoreChannel(), None, "{} is now banned".format(text))
  actionQueue.flush()
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
  lines = open('{}_logfile.txt'.format(underscoreChannel()), 'r').read().splitlines()
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
    modal = Modal('profile', trigger, user)
    modal.open()
  
  return Response(), 200

#handle Civ VI payloads for turn notifications in the "play by cloud" game mode
@app.route('/civ', methods=['POST'])
def civ():
  actionQueue = ActionQueue()
  data = request.get_json(force=True)
  currentPlayer = data.get('value2')
  
  f = open('last_civ_webhook_payload.txt', 'r')
  lastPayload = f.read()
  f.close()
  
  f = open('last_civ_webhook_payload.txt', 'w')
  f.write(str(data))
  f.close()
  
  if str(data) == lastPayload:
    return Response(), 200
  
  gameToChannelMap = {
    'Slaughter of the Lamb': ch.civSlaughterChannel(),
    "Beerdeau's Game": ch.civBeerdeauChannel(),
    '2 Front War': ch.civTwoFrontWarChannel(),
    "lackmind's Game": ch.civLackChannel(),
    'Hide From Sumeria': ch.civHideFromSumeria(),
    'mod-pilot': ch.civModPilot()
  }
  
  actionQueue.addReply(
    'Civ',
    gameToChannelMap.get(data.get('value1'), ch.civChannel()), 
    None, 
    '{}: <@{}> it is your turn! (turn {})'.format(data.get('value1'), STEAM.get(currentPlayer), data.get('value3')), 
    Identity(userName = 'Civilization VI: Turn Notification', emoji = 'civ6')
  )
  actionQueue.flush()
  return Response(), 200
  
if __name__ == "__main__":
  app.run()
