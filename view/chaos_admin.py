from view._view import View

class ChaosAdminView(View):
  
  def __init__(self, user):
    super().__init__(user)    
  
    
  def build(self):
    self.setTitle('Chaos Admin')
    threadUsersCursor = user._db.users.find({'threads': True})
    options = []
    for threadUser in threadUsersCursor:
      options.append(
        {
          "text": {
            "type": "plain_text",
            "text": threadUser.get('profile').get('display_name'),
            "emoji": True
          },
          "value": "wizarding",
          "description": {
            "type": "plain_text",
            "text": "I would like to participate in magical duals",
            "emoji": True
          }
        }
      )
                                     
    element = {
      "type": "checkboxes",
      "options": self.getAllOptions(),
    }
    if selectedOptions:
      element['initial_options'] = selectedOptions
    self._blocks.append(
      {
        "type": "actions",
        "elements": [element]
      }
    )
    return
    
    
    self._finalize()
    return self.view
  
 

