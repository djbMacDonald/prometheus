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
    threadUsersCursor = self.user._db.users.find({'threads': True})
    options = []
    for threadUser in threadUsersCursor:
      name = threadUser.get('profile').get('real_name')
      options.append(
        {
          "text": {
            "type": "plain_text",
            "text": name,
            "emoji": True
          },
          "value": threadUser.get('id')
        }
      )
                                     
    element = {
      "type": "checkboxes",
      "options": options
    }
  
    self._blocks.append(
      {
        "type": "actions",
        "elements": [element]
      }
    )
    

