import os

class Emote:
  
  def __init__(self, emotes):
    self._emotes = emotes
    
  def getAll(self):
    return self._emotes
  
  def getReactionsOnPost(self, event):
    postData = {
      'token': os.environ.get('SECRET'),
      'channel': self._event.channel(),
      'latest': self._event.id(),
      'inclusive': True,
      'oldest': self._event.id()
    }
#     req = requests.get('https://slack.com/api/channels.history?{}'.format(urllib.parse.urlencode(postData)))
    
#     message = req.json().get('messages')
#     if not message or len(message) < 1:
#       return
#     message = message[0]
#     if message.get('replies') or message.get('thread_ts'):
#       return
#     if not message.get('reactions'):
#       return
    
#     reactionNames = map(lambda reaction: reaction.get('name'), message.get('reactions'))