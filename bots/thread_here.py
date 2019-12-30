from utils.post import PostUtil
import random
from model.identity import Identity
import urllib
import requests
import os

class ThreadHereBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
  
  def run(self):
    if self._event.isFromABot() or not self._event.threadId() or not self._event.:
      return;
    messages = self._checkForReplies()
    if not messages or not messages[0] or not messages[0]['reply_count'] or messages[0]['reply_count'] < 3
      return
      
#   move to utils
  def _checkForReplies():
    postData = {
      'token': os.environ.get('SECRET'),
      'channel': self._event.channel(),
      'thread_ts': self._event.threadId()
      'channel': self._event.channel(),
      'latest': self._event.id(),
      'inclusive': True,
      'oldest': self._event.id()
    }
    req = requests.get('https://slack.com/api/channels.replies?{}'.format(urllib.parse.urlencode(postData)))
    return req.json().get('messages')

# function notifyMissingUsers(threadId, user, channel, users) {
#   var number =  Math.floor(Math.random() * 10); 
  
#   if (number !== 2 || channel !== 'CDR5ZBTT7' || users.length === names.length) {
#     return
#   }
  
#   var usersNotIncluded = allOfUs.filter(function(currentUser){
#     return users.indexOf(currentUser) === -1;
#   });
  
#   var options = {
#     host: 'www.slack.com',
#     path: '/api/chat.postMessage',
#     method: 'POST',
#     headers: {
#       'Content-Type': 'application/json; charset=utf-8',
#       'Authorization': 'Bearer ' + process.env.SECRET
#     }
#   };
#   var str = ''
#   //dave = UDBGH9BMX
#   var req = https.request(
#     options,
#     function (resp) {
#       //no-op
#     }
#   );
  
#   req.on('error', function (err) {
#       console.log('error: ' + err);
#   });
  
#   var userMap = usersNotIncluded.map((currentUser) => {
#     return '<@' + currentUser + '>'
#   });
  
#   //This is the data we are posting, it needs to be a string or a buffer
#   req.write(JSON.stringify({
#     channel: channel,
#     link_names: 1,
#     thread_ts: threadId,
#     as_user: false,
#     user: user,
#     username: 'Chaos Seed',
#     icon_emoji: ':chaos:',
#     text: 'Hey ' + userMap.join(', ') + '! Theres a thread here!',
#     response_type: 'in_channel'
#   }));
  
#   parentThreads.splice(parentThreads.indexOf(threadId),1);
  
#   //UDC03KCGK drew
#   //UDC4QL95G Dakota
#   //UDDE5960N CJ
#   //UDBGH9BMX Dave
#   req.end();
# }