import os
import requests
import urllib

class Emote:
  
  def __init__(self, emotes):
    self._emotes = emotes
    
  def getAll(self):
    return self._emotes
  
  def getReactionsOnPost(self, event):
    postData = {
      'token': os.environ.get('SECRET'),
      'channel': event.channel(),
      'latest': event.id(),
      'inclusive': True,
      'oldest': event.id()
    }
    req = requests.get('https://slack.com/api/channels.history?{}'.format(urllib.parse.urlencode(postData)))
    
    messages = req.json().get('messages')
    if not messages or len(messages) < 1 or not messages[0].get('reactions'):
      return []
    reactionNames = map(lambda reaction: reaction.get('name'), messages[0].get('reactions'))
    return {'text': messages[0].get('text'), 'reactionNames': reactionNames}