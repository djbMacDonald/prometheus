from utils.post import PostUtil
import random
import requests
from utils.channel import ChannelUtil
from constant.creepy import STATEMENT_GENERATOR
from constant.people import CHAOS_USERS

class SummonBot:
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
    self._channelUtil = ChannelUtil()
  
  def run(self):
    if not self._event.text() or not self._event.text().lower() == "summon the silent" or not self._event.isPartOfAThread():
      return
    threadJson = self._channelUtil.getThreadData(self._event.channel(), self._event.threadId())
    silentUsers = list(set(CHAOS_USERS.values()) - set(threadJson['messages'][0]['reply_users']))
    message = '';
  
    creepyNouns, creepyFacts, creepyActs, creepyEnds = STATEMENT_GENERATOR
    random.shuffle(creepyNouns)
    random.shuffle(creepyFacts)
    random.shuffle(creepyActs)
    random.shuffle(creepyEnds)
  
    for index in range(len(silentUsers)):
      message += '<@' + silentUsers[index] + '>\n'
      message += self._generateOminousStatement(creepyNouns[index], creepyFacts[index], creepyActs[index], creepyEnds[index])
      message += '\n\n'
    self._postUtil.addMessageToThread(message, self._event.channel(), self._event.threadId())
  
  def _generateOminousStatement(self, noun, fact, act, end):
    message = noun + ' ' + fact + '\n' + act + ' ' + end
    return message;
