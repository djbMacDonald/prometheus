import jsons
from constant.channels import CHANNELS
from model.caster import Caster
from view.cast import CastView
from model.modal import updateModal
from multiprocessing import Pool
from view.chaos import ChaosView
from view.chaos_admin import ChaosAdminView
from model.user import User
from utils.view_factory import ViewFactory

from utils.post import Post
class SlackEvent:
  def __init__(self, event):
    
    if not event.get('type'):
      return
    
    type, user_id, timestamp = event.get('view').get('external_id').split('~')
    
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
        #post.addMessageToChannel(shame, channel = CHANNELS['Chaos'])

      
    if event.get('type') == 'block_actions':
      view = ViewFactory.getView(type)
      view.handleAction(user_id, event, timestamp)
        
    else:
      print(event.get('type'))



  def getChannelId(self):
    return self.channel.get('id')
  
  def getChannelName(self):
    return self.channel.get('name')
  
  def getUserId(self):
    return self.user.get('id')