import os

class PostData:
  
  def __init__(self, channel, message, identity, impersonate = False, threadId = None):
    self.params = {
      'token': os.environ.get('SECRET'),
      'channel': channel,
      'text': message,
      'as_user': impersonate,
    }
    if threadId:
      self.params['thread_ts'] = threadId
    if identity and identity.userName():
      self.params['username'] = identity.userName()
    if identity and identity.profilePicture():
      self.params['icon_url'] = identity.profilePicture()
  
  def get(self):
    return self.params