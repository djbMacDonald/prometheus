import random
from constant.creepy import STATEMENT_GENERATOR
from constant.people import impersonations
from bots._bot import Bot

class Summon(Bot):
  
  _active = True
  
  @classmethod
  def description(cls):
    return "If you say 'summon the silent' in a thread, then will ping all Chaos users with weird stuff."
  
  def run(self):
    if not self._event.text() or not self._event.text().lower() == "summon the silent" or not self._event.isPartOfAThread():
      return
    threadJson = self._channelUtil.getThreadData(self._event.channel(), self._event.threadId())
    chaosPeople = set(map(lambda person: person.get('id'), impersonations()))
    silentUsers = list(chaosPeople - set(threadJson['messages'][0]['reply_users']))
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
    self._postUtil.addMessageToThread(message)
  
  def _generateOminousStatement(self, noun, fact, act, end):
    message = noun + ' ' + fact + '\n' + act + ' ' + end
    return message;
