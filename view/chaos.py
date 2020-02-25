from view._view import View

class ChaosView(View):
  
  def __init__(self, user):
    super().__init__(user)
    self.external_id = 'chaos'
    
  def build(self):
    self.setTitle('Chaos Preferences')
    self._buildPreferences()
    self._finalize()
    return self.view
  
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
  
  def getWizardOption(self):
    return {
							"text": {
								"type": "plain_text",
								"text": "Wizarding"
							},
							"value": "wizarding",
							"description": {
								"type": "plain_text",
								"text": "I would like to participate in magical duals"
							}
						}
  def getThreadOption(self):
    return {
							"text": {
								"type": "plain_text",
								"text": "Thread Notifications"
							},
							"value": "threads",
							"description": {
								"type": "plain_text",
								"text": "I would like to recieve notifications in active threads from Chaos Seed"
							}
						}

  def getImpersonationOption(self):
    return {
							"text": {
								"type": "plain_text",
								"text": "Bot Impersonations"
							},
							"value": "impersonations",
							"description": {
								"type": "plain_text",
								"text": "I would like to be eligibile for a bot impersonation"
							}
						}

  def getAllOptions(self):
    return [self.getThreadOption(), self.getImpersonationOption(), self.getWizardOption()]
  
  def handleAction(self, action, ts):
    print(action)
    self.user.wizard = self.getWizardOption() in action.get('selected_options')
    self.user.doppleganger = self.getImpersonationOption() in action.get('selected_options')
    self.user.threads = self.getThreadOption() in action.get('selected_options')
    self.user.update(ts)
    return
