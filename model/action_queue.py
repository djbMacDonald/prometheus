from constant.channels import ALLOWED_CHANNELS
import os
import urllib
import requests
from model.post_data import PostData
from utils.log import Log

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
  
  def shouldDelete():
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
    for reactionRequest in self._reactions:
      self._flushReactions(reactionRequest)
    return
  
  def _isAllowedToPostInThisChannel(self, channel):
    print(channel)
    print(ALLOWED_CHANNELS)
    return channel in ALLOWED_CHANNELS
  
  def _flushReactions(self, reactionRequest):
    if not self._isAllowedToPostInThisChannel(reactionRequest.get('channel')):
      return
    options = {
      'channel': channel,
      'name': reaction, 
      'timestamp': timestamp,
      'as_user': False,
      'token': os.environ.get('DAKA')
    }
    url = 'https://www.slack.com/api/reactions.add?{}'.format(urllib.parse.urlencode(options))
    self._log.logEvent("{}: {}-bot adds reaction: {}".format(self._event.channelName(), self._caller, reaction))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)