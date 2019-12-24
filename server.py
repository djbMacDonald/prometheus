from flask import Flask, request, render_template, jsonify, Response
from multiprocessing import Pool
import json

from model.event import Event

from bots.dm import DmBot
from bots.scrambler import ScramblerBot

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
  originalEvent = Event(data)
  
  bots = [
      DmBot(originalEvent, pool),
      ScramblerBot(originalEvent, pool)
    ]
    
  for bot in bots:
    result = bot.run()
    if result == 'end':
      return data, 200
    
  return data, 200

if __name__ == "__main__":
  app.run()
