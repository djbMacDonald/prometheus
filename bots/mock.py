from model.identity import Identity
from bots._bot import Bot
import json

class Mock(Bot):
  _active = True
  
  @classmethod
  def description(cls):
    return "If you use the spongebob-mock emote on a message,  it will post to a thread that weird alternating caps thing version of the message."
  
  def run(self):
    if self._event.isAMessage() or self._event.isPartOfAThread():
      return
    
    messageInfo = self._emoteUtil.getReactionsOnPost(self._event)
    if not messageInfo or not messageInfo.get('reactionNames'):
      return
    intersection = set(messageInfo.get('reactionNames')).intersection(['spongebob-mock', 'mocking-spongebob'])
    if len(intersection) == 0 or messageInfo.get('hasAThread'):
      return
    self._addMessageToThread(self._mockString(messageInfo.get('text')), Identity('sPoNgeBoB', 'https://emoji.slack-edge.com/TDBEDSEQZ/spongebob-mock/3b66c2fdf2b77a8d.png'))
    
  def _mockString(self, string):
    return "".join(map(
      lambda charTuple: charTuple[1].lower() if charTuple[0] % 2 else charTuple[1].upper(), 
      enumerate(string)
    ))
