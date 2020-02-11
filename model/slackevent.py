import jsons
from dataclasses import dataclass


@dataclass
class SlackEvent:
  
  type: str
  actions: list
  team: dict
  channel: dict
  user: dict
  action_ts: float
  message_ts: float
  attachment_id: str
  token: str
  is_app_unfurl: bool
  response_url: str
  trigger_id: str
  callback_id: str = None


  def getChannelId(self):
    return self.channel.get('id')
  
  def getChannelName(self):
    return self.channel.get('name')
  
  def getUserId(self):
    return self.user.get('id')