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
    if self._event.isFromABot():
      return;
    
    
    # if (!request.body.event.thread_ts) {
    #   parentThreads[(threadIndex++ % 100)] = request.body.event.ts
    # } else {
    #   if (parentThreads.includes(request.body.event.thread_ts)) {
    #     //testMessage(request.body.event.ts);
    #     checkForReplies(request.body.event.thread_ts, request.body.event.channel, request.body.event.user);
    #     response.json({});  
    #     return;
    #   }
    
    function checkForReplies(threadId, channel, user) {
  let url = 'https://www.slack.com/api/channels.replies?token=' + process.env.SECRET + '&thread_ts=' + threadId + '&channel=' + channel;
  https.get(url, function (res) {
      var jsonRetval = '';
      res.on('data', (d) => {
        jsonRetval += d.toString();
      });
      res.on('end', (d) => {
        //console.log(jsonRetval);
        var message = (JSON.parse(jsonRetval));
        //console.log(message);
        if (message.messages[0].reply_count > 3) {
          //askToPingDave(threadId, user, channel, message.messages[0].reply_users);
          notifyMissingUsers(threadId, user, channel, message.messages[0].reply_users);
        }
      });
  });
  
}

function notifyMissingUsers(threadId, user, channel, users) {
  var number =  Math.floor(Math.random() * 10); 
  
  if (number !== 2 || channel !== 'CDR5ZBTT7' || users.length === names.length) {
    return
  }
  
  var usersNotIncluded = allOfUs.filter(function(currentUser){
    return users.indexOf(currentUser) === -1;
  });
  
  var options = {
    host: 'www.slack.com',
    path: '/api/chat.postMessage',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Authorization': 'Bearer ' + process.env.SECRET
    }
  };
  var str = ''
  //dave = UDBGH9BMX
  var req = https.request(
    options,
    function (resp) {
      //no-op
    }
  );
  
  req.on('error', function (err) {
      console.log('error: ' + err);
  });
  
  var userMap = usersNotIncluded.map((currentUser) => {
    return '<@' + currentUser + '>'
  });
  
  //This is the data we are posting, it needs to be a string or a buffer
  req.write(JSON.stringify({
    channel: channel,
    link_names: 1,
    thread_ts: threadId,
    as_user: false,
    user: user,
    username: 'Chaos Seed',
    icon_emoji: ':chaos:',
    text: 'Hey ' + userMap.join(', ') + '! Theres a thread here!',
    response_type: 'in_channel'
  }));
  
  parentThreads.splice(parentThreads.indexOf(threadId),1);
  
  //UDC03KCGK drew
  //UDC4QL95G Dakota
  //UDDE5960N CJ
  //UDBGH9BMX Dave
  req.end();
}