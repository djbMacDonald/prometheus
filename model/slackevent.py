import jsons
from dataclasses import dataclass


@dataclass
class SlackEvent:
  
  type: str
  actions: list
  team: dict
  user: dict
  token: str
  trigger_id: str
  view: dict = None
  response_url: str = None
  is_app_unfurl: bool = None
  attachment_id: str = None
  message_ts: float = None
  action_ts: float = None
  channel: dict = None
  callback_id: str = None

  def getChannelId(self):
    return self.channel.get('id')
  
  def getChannelName(self):
    return self.channel.get('name')
  
  def getUserId(self):
    return self.user.get('id')