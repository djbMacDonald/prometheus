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
    print (j)
    return self.view
  
  def handleAction(self, action, ts):
    print(action.get('selected_options'))
    return
  
  def buildThreadUsers(self):
    threadUsersCursor = self.user._db.users.find()
    options = []
    selectedOptions = []
    for threadUser in threadUsersCursor:    
      for key, value in threadUser.items():
        option = {
            "text": {
              "type": "plain_text",
              "text": key,
              "emoji": True
            },
            "value": value
        }
        options.append(option)
        if threadUser.get('threads'):
          selectedOptions.append(option)
                                     
    element = {
      "type": "checkboxes",
      "options": options,
    }
    
    
    if selectedOptions:
      element['initial_options'] = selectedOptions
  
    self._blocks.append(
      {
        "type": "actions",
        "elements": [element]
      }
    )
