from view._view import View
import time

class ChaosAdminView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.external_id = 'chaos_admin'
  
    
  def build(self):
    self.setTitle('Chaos Admin')
    self.buildThreadUsers()
    self._finalize()
    return self.view
  
 
  def buildThreadUsers(self):
    threadUsersCursor = self.user._db.users.find()
    options = []
    selectedOptions = []
    self.addDivider()
    for threadUser in threadUsersCursor:      
      name = threadUser.get('profile').get('real_name')

  
      self.add(
        {
          "type":"section",
           "text":{ 
              "type":"mrkdwn",
              "text":f"*{name}* \n> *Thread User:* {':check:' if threadUser.get('threads') else ':x:'}"
           },
          "accessory": {
            "type": "overflow",
            "options": [
              {  
                "text": {
                  "type": "plain_text",
                  "text": ":pencil: Edit",
                  "emoji": True
                },
                "value": f"edit~{threadUser.get('id')}~{time.time()}"
              },
              {
                "text": {
                  "type": "plain_text",
                  "text": ":x: Delete",
                  "emoji": True
                },
                "value": f"edit~{threadUser.get('id')}~{time.time()}"
              }
            ]
          }
        }
      )
      self.addDivider()
    
  def handleAction(self, user_id, event, ts):
    
    print(event.get('actions')[0].get('selected_option').get('value'))
    return

