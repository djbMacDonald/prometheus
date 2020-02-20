import jsons




class SlackEvent:
  def __init__(self, event):
    
    if not event.get('type'):
      return
    
    if event.get('type') =='view_submission':
      print('view submission')
      
    if event.get('type') == 'block_actions':
      print('block_action')
      print(event)
      
      
    else:
      print(event.get('type'))
      
    """
    type: str = None
    actions: list = None
    view: dict = None
    response_url: str = None
    is_app_unfurl: bool = None
    attachment_id: str = None
    message_ts: float = None
    action_ts: float = None
    channel: dict = None
    callback_id: str = None
    actions: list = None
    team: dict = None
    user: dict = None
    token: str = None
    trigger_id: str = None
    """


  def getChannelId(self):
    return self.channel.get('id')
  
  def getChannelName(self):
    return self.channel.get('name')
  
  def getUserId(self):
    return self.user.get('id')