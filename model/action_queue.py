from constant.channels import allowed_channel_ids, CHANNELS
import os
import urllib
import requests
from model.post_data import PostData
from utils.log import Log
import random
from utils.emote import Emote
from multiprocessing import Pool
from constant.channels import allowed_channel_ids

def poolCallback(args):
  args.close()
  return

class ActionQueue:
  
  def __init__(self, pool = None, event = None):
    self._log = Log()
    if pool:
      self._pool = pool
    else:
      self._pool = Pool(1)
    self._originalEvent = event
    
    self._replacements = []
    self._replies = []
    self._reactions = []
    self._commands = []
    
  def addReplacement(self, bot, channel, id, thread, message, identity = None):
    if not self._isAllowedToPostInThisChannel(channel):
      return;
    self._replacements.append({'bot': bot, 'channel': channel, 'id': id, 'threadId': thread, 'message': message, 'identity': identity})
  
  def addReaction(self, bot, channel, timestamp, reaction):
    if not self._isAllowedToPostInThisChannel(channel):
      return;
    self._reactions.append({'bot': bot, 'channel': channel, 'timestamp': timestamp, 'reaction': reaction})
  
  def addReply(self, bot, channel, thread, message, identity = None):
    if not self._isAllowedToPostInThisChannel(channel):
      return;
    self._replies.append({'bot': bot, 'channel': channel, 'threadId': thread, 'message': message, 'identity': identity})
    
  def addCommand(self, bot, channel, command, message, identity = None):
    if not self._isAllowedToPostInThisChannel(channel):
      return;
    self._commands.append({'bot': bot, 'channel': channel, 'command': command, 'message': message, 'identity': identity})
  
  def flush(self):
    if self._replacements:
      self._flushReplacement(random.choice(self._replacements))
      
    replyRequests = self._replies
    random.shuffle(replyRequests)
    for replyRequest in self._replies:
      self._flushReply(replyRequest)
      
    for reactionRequest in self._reactions:
      self._flushReaction(reactionRequest)
      
    for commandRequest in self._commands:
      self._flushCommand(commandRequest)
      
    self._replacements = []
    self._replies = []
    self._reactions = []
    self._commands = []
    
    self._pool.close()
    self._pool.join()
    
  def _isAllowedToPostInThisChannel(self, channel):
    return channel in allowed_channel_ids()
  
  def _flushReplacement(self, replacementRequest):
    postData = PostData(
      replacementRequest.get('channel'), 
      replacementRequest.get('message'), 
      replacementRequest.get('identity'), 
      threadId = replacementRequest.get('threadId')
    )
    info = postData.get()
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.parse.urlencode(info))
    try:
      res = self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
      newTS = res.get(timeout=1).json()['ts']
      
      for reactionRequest in self._reactions:
        if reactionRequest.get('timestamp') == replacementRequest.get('id'):
          reactionRequest['timestamp'] = newTS
      for replyRequest in self._replies:
        if replyRequest.get('threadId') == replacementRequest.get('id'):
          replyRequest['timestamp'] = newTS

      self._log.logEvent("{}: {}-bot adds message: {}".format(CHANNELS[replacementRequest.get('channel')].get('name'), replacementRequest.get('bot'), info['text']))
      self._deleteMessage(replacementRequest)
    except Exception as error:
      print('Error with replacement')
  
  def _flushReply(self, replyRequest):
    postData = PostData(replyRequest.get('channel'), replyRequest.get('message'), replyRequest.get('identity'), threadId = replyRequest.get('threadId'))
    info = postData.get()
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.parse.urlencode(info))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    self._log.logEvent("{}: {}-bot adds message: {}".format(CHANNELS[replyRequest.get('channel')].get('name'), replyRequest.get('bot'), info['text']))
  
  def _flushReaction(self, reactionRequest):
    options = {
      'channel': reactionRequest.get('channel'),
      'name': reactionRequest.get('reaction'), 
      'timestamp': reactionRequest.get('timestamp'),
      'as_user': False,
      'token': os.environ.get('DAKA')
    }
    url = 'https://www.slack.com/api/reactions.add?{}'.format(urllib.parse.urlencode(options))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    self._log.logEvent("{}: {}-bot adds reaction: {}".format(CHANNELS[reactionRequest.get('channel')].get('name'), reactionRequest.get('bot'), reactionRequest.get('reaction')))
    
  def _flushCommand(self, commandRequest):
    return
    postData = PostData(
      commandRequest.get('channel'), 
      commandRequest.get('message'), 
      commandRequest.get('identity'), 
      command = commandRequest.get('command')
    )
    info = postData.get()
    url = 'https://www.slack.com/api/chat.postMessage?{}'.format(urllib.parse.urlencode(info))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    self._log.logEvent("{}: {}-bot uses command: {}".format(CHANNELS[reactionRequest.get('channel')].get('name'), commandRequest.get('bot'), commandRequest.get('command')))
  
  def _deleteMessage(self, replacementRequest):
    postData = {
       'channel': replacementRequest.get('channel'),
       'ts': replacementRequest.get('id'),
       'token': os.environ.get('SECRET')
    }
    url = 'https://www.slack.com/api/chat.delete?{}'.format(urllib.parse.urlencode(postData))
    self._pool.apply_async(requests.get, args=[url], callback=poolCallback)
    self._log.logEvent("{}: {}-bot deletes message: {}".format(CHANNELS[replacementRequest.get('channel')].get('name'), replacementRequest.get('bot'), self._originalEvent.text()))
