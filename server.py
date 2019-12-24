from flask import Flask, request, render_template, jsonify, Response
from multiprocessing import Pool

from model.event import Event

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
  
  
  
  return data

if __name__ == "__main__":
  app.run()
