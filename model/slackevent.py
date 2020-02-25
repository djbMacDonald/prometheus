import jsons
from constant.channels import CHANNELS
from model.caster import Caster
from view.cast import CastView
from model.modal import updateModal
from multiprocessing import Pool
from view.chaos import ChaosView
from model.user import User

from utils.post import Post
class SlackEvent:
  def __init__(self, event):
    
    if not event.get('type'):
      return
    
    type, user_id, timestamp = event.get('view').get('external_id').split('_')
    
    if event.get('type') =='view_submission':
      if type == 'cast':
        view = CastView(None, user_id)
        target = event.get('view').get('state').get('values').get('cast_targets').get('selected_cast_target').get('selected_option').get('text').get('text')
        user_id = event.get('user').get('id')
        print(target)
        spell = event.get('view').get('private_metadata')
        caster = Caster(user_id)
        shame = f"{caster.name} just tried to cast {spell} on {target} but failed... cuz they are bad."
        #post = Post(Pool(1))
        #post.addMessageToChannel(shame, CHANNELS['Chaos'])

      
    if event.get('type') == 'block_actions':
      user = User(None, None, user_id)
      
      if type == 'cast':
        view = CastView(user)
        view.handleAction(event.get('actions'))
        view = view.build()
        updateModal(event.get('view').get('external_id'), view)
        
      if type == 'chaos':
        view = ChaosView(user)
        view.handleAction(event.get('actions')[0], event.get('action_ts'))      
        return
      
      if type == 'ChaosAdmin':
        view = ChaosAdminView(user)
        view.handleAction(event.get('actions')[0], event.get('action_ts'))


        
      
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