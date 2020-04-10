from constant.channels import allowed_channel_ids, CHANNELS
import os
import urllib
import requests
from model.post_data import PostData
from utils.log import Log
import random

def poolCallback(args):
  # print('test', args)
  args.close()
  return

class ActionQueue:
  
  _replacements = []
  _replies = []
  _reactions = []
  
  def __init__(self, pool):
    self._log = Log()
    self._pool = pool
  
  def shouldDelete(self):
    return
  
  def replacement(self):
    return
  
  def replies(self):
    return
  
  def addReaction(self, bot, channel, timestamp, reaction):
    self._reactions.append(
      {'bot': bot, 'channel': channel, 'timestamp': timestamp, 'reaction': reaction}
    )
    return
  
  def reactions(self):
    return
  
  def flush(self):
    replyRequests = self._replies
    random.shuffle(replyRequests)
    
    if self._replacements:
      self._flushReplacement(random.choice(self._replacements))
    for replyRequest in self._replies:
      self._flushReply(replyRequest)
    for reactionRequest in self._reactions:
      self._flushReaction(reactionRequest)
  
  def _flushReplacement(self, replacementRequest):
    return
  
  def _flushReply(self, replyRequest):
    return
  
  def _flushReaction(self, reactionRequest):
    options = {
      'channel': reactionRequest.get('channel'),
      'name': reactionRequest.get('reaction'), 
      'timestamp': reactionRequest.get('timestamp'),
      'as_user': False,
      'token': os.environ.get('DAKA')
    }
    url = 'https://www.slack.com/api/reactions.add?{}'.format(urllib.parse.urlencode(options))
#     change to channel name
    self._log.logEvent("{}: {}-bot adds reaction: {}".format(CHANNELS[reactionRequest.get('channel')].get('name'), reactionRequest.get('bot'), reactionRequest.get('reaction')))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
