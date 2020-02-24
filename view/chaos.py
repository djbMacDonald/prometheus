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
    if self.user.isAWizard():
      selectedOptions.append(self.getWizardOption())
    if self.user.notifyOnThreads():
      self.selectedOptions.append(self.getThreadOption())
    if self.user.hasDoppleganger():
      self.selectedOptions.append(self.getImpersonationOption()
                                 
    options = [self.getThreadOption(), self.getImpersonationOption(), self.getWizardOption()]
    
    
    self._blocks.append(
      {
			"type": "actions",
			"elements": [
				{
					"type": "checkboxes",
					"options": [
					
					
						
            ],
          'initial_options': [
            {
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
          ]
          }
        ]
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

