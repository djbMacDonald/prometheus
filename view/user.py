from view._view import View

class UserView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.external_id = 'user'
    
  def build(self):
    self.setTitle('User Management')
    self._finalize()
    return self.view
  
  def handleAction(self, action, ts):
    print(action.get('selected_options'))
    return
