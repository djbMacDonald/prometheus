from flask import Flask, request, render_template, jsonify, Response
from multiprocessing import Pool
import json

from model.event import Event

from bots.scrambler import ScramblerBot
from bots.nice import NiceBot
from bots.dm import DmBot
from bots.mock import MockBot
from bots.underscore import UnderscoreBot
from bots.stabby import StabbyBot
from bots.fire import FireBot
from bots.hello import HelloBot
from bots.summon import SummonBot
from bots.pig import PigBot
from bots.space_replace import SpaceReplaceBot
from bots.reminder import ReminderBot
from bots.dnd import DndBot
from bots.say_again import SayAgainBot
from bots.new_ban import NewBanBot
from bots.group_call import GroupCallBot
from bots.ban_list import BanListBot
from bots.deja_vu import DejaVuBot
from bots.botify import BotifyBot

app = Flask(__name__)

handledEvents = [];
bans = {}

@app.route("/listen", methods=['POST'])
def inbound():
  data = request.get_json(force=True)
  
  print(json.dumps(data, indent=2, sort_keys=True))
  
  if data.get('event_id') in handledEvents or not data.get('event'):
    return data, 200
  else:
    handledEvents.append(data.get('event_id'))
  
  pool = Pool(1)
  originalEvent = Event(data, bans)
  
  bots = [
      DmBot(originalEvent, pool), 
      MockBot(originalEvent, pool), 
      NiceBot(originalEvent, pool), 
      UnderscoreBot(originalEvent, pool),
      StabbyBot(originalEvent, pool),
      FireBot(originalEvent, pool),
      HelloBot(originalEvent, pool),
      SummonBot(originalEvent, pool),
      PigBot(originalEvent, pool),
      ScramblerBot(originalEvent, pool),
      SpaceReplaceBot(originalEvent, pool),
      ReminderBot(originalEvent, pool),
      DndBot(originalEvent, pool),
      SayAgainBot(originalEvent, pool),
      NewBanBot(originalEvent, pool),
      GroupCallBot(originalEvent, pool),
      BanListBot(originalEvent, pool),
      DejaVuBot(originalEvent, pool),
      BotifyBot(originalEvent, pool)
    ]
    
  for bot in bots:
    result = bot.run()
    if result == 'end':
      return data, 200
    
  return data, 200

if __name__ == "__main__":
  app.run()
