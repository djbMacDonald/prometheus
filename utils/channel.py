import os
import json
import requests

# move to static functions
class ChannelUtil:
  
  def getThreadData(self, channel, threadTs):
    if not threadTs:
      return None
    url = 'https://www.slack.com/api/channels.replies?token=' + os.environ.get('SECRET') + '&thread_ts=' + threadTs + '&channel=' + channel
    request = requests.get(url);
    return request.json()
  
  def getChannelData(self, channel):
    url = 'https://www.slack.com/api/channels.history?token=' + os.environ.get('SECRET') + '&channel=' + channel
    request = requests.get(url);
    return request.json()