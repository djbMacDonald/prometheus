from view._view import View
import json

class ProfileView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.external_id = 'user'
    
  def build(self):
    self.setTitle('User Management')
    self.buildThreadUsers()
    self._finalize()
    return self.view
  
  def handleAction(self, action, ts):
    print(action.get('selected_options'))
    return
  
  def buildThreadUsers(self):
    threadUsersCursor = self.user._db.users.find()
    options = []
    selectedOptions = []
    text = ""
    
          
     
    
    
   
    
