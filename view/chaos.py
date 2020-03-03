from view._view import View
from constant.view import DIVIDER


class ChaosView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.external_id = 'chaos'
    
  def build(self):
    self.setTitle('Chaos Preferences')
    self.setMetadata(self.user.id)
    self._buildStatus()
    self._buildPreferences()
    return super().build()
  
  def _buildPreferences(self):
    selectedOptions = []
    if self.user.notifyOnThreads():
      selectedOptions.append(self.getThreadOption())
    if self.user.hasDoppleganger():
      selectedOptions.append(self.getImpersonationOption())
    if self.user.isWizard():
      selectedOptions.append(self.getWizardOption())
                                     
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
  def _buildStatus(self):
    dopple = f"*Dopple:*{self.user.doppleName}" if hasattr(self.user, 'doppleName') else ""
    self._blocks.append({ 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text":f"*Name:* {self.user.real_name}\n{f"*Dopple:*{self.user.doppleName}" if hasattr(self.user, 'doppleName') else ""}
         },
         "accessory":{ 
            "type":"image",
            "image_url":self.user.profile.get('image_original'),
            "alt_text":"Airstream Suite"
         }
    })
    self._blocks.append(DIVIDER)
  
  def getWizardOption(self):
    return {
							"text": {
								"type": "plain_text",
								"text": "Wizarding",
                "emoji": True
							},
							"value": "wizarding",
							"description": {
								"type": "plain_text",
								"text": "I would like to participate in magical duals",
                "emoji": True
							}
						}
  def getThreadOption(self):
    return {
							"text": {
								"type": "plain_text",
								"text": "Thread Notifications",
                "emoji": True
							},
							"value": "threads",
							"description": {
								"type": "plain_text",
								"text": "I would like to recieve notifications in active threads from Chaos Seed",
                "emoji": True
							}
						}

  def getImpersonationOption(self):
    return {
							"text": {
								"type": "plain_text",
								"text": "Bot Impersonations",
                "emoji": True
							},
							"value": "impersonations",
							"description": {
								"type": "plain_text",
								"text": "I would like to be eligibile for a bot impersonation",
                "emoji": True
							}
						}

  def getAllOptions(self):
    return [self.getThreadOption(), self.getImpersonationOption(), self.getWizardOption()]
  
  def handleAction(self, user_id, event, ts):
    action = event.get('actions')[0]
    self.setUser(user_id)
    print(action.get('selected_options'))
    print(self.getThreadOption())
    self.user.wizard = self.getWizardOption() in action.get('selected_options')
    self.user.doppleganger = self.getImpersonationOption() in action.get('selected_options')
    self.user.threads = self.getThreadOption() in action.get('selected_options')
    self.user.update(ts)
    return
