import jsons
from dataclasses import dataclass


@dataclass
class SlackEvent:
  type: str
  actions: list
  callback_id: str
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