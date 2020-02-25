from view._view import View

class ChaosAdminView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.external_id = 'ChaosAdmin'
  
    
  def build(self):
    self.setTitle('Chaos Admin')
    self.buildThreadUsers()
    self._finalize()
    return self.view
  
 
  def buildThreadUsers(self):
    threadUsersCursor = self.user._db.users.find()
    options = []
    selectedOptions = []
    for threadUser in threadUsersCursor:
      
      print (threadUser)
      
      name = threadUser.get('profile').get('real_name')
      option = {
          "text": {
            "type": "plain_text",
            "text": name,
            "emoji": True
          },
          "value": threadUser.get('id')
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
    
  def handleAction(self, actions, timestamp):
    
    return

