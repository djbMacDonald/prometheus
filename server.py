from flask import Flask, request, render_template, jsonify, Response
from multiprocessing import Pool

from model.event import Event

from bots.dm import DmBot
from bots.scrambler import ScramblerBot

app = Flask(__name__)

handledEvents = [];

@app.route("/listen", methods=['POST'])
def inbound():
  data = request.get_json(force=True)
  
  if (data.get('event_id') in handledEvents):
    return
  else:
    handledEvents.append(data.get('event_id'))
    
  print(json.dumps(data, indent=2, sort_keys=True))
  
  pool = Pool(1)
  originalEvent = Event(data)
  
  bots = [
      DmBot(originalEvent, pool),
      ScramblerBot(originalEvent, pool)
    ]
    
  for bot in bots:
    result = bot.run()
    if result == 'end':
      return Response(), 200
    
  return Response(), 200

if __name__ == "__main__":
  app.run()
