from view._view import View

class ChaosView(View):
  
  def __init__(self, user):
    super().__init__(req)
    self.external_id = 'chaos'
    
  def build(self):
    self.setTitle('Chaos Preferences')
    self._buildPreferences()
    self._finalize()
    return self.view
  
  def _buildPreferences(self):
    self._blocks.append(
      {
			"type": "actions",
			"elements": [
				{
					"type": "checkboxes",
					"options": [
						{
							"text": {
								"type": "plain_text",
								"text": "Thread Notifications"
							},
							"value": "tasks",
							"description": {
								"type": "plain_text",
								"text": "I would like to recieve notifications in active threads from Chaos Seed"
							}
						},
						{
							"text": {
								"type": "plain_text",
								"text": "Bot Impersonations"
							},
							"value": "comments",
							"description": {
								"type": "plain_text",
								"text": "I would like to be eligibile for a bot impersonation"
							}
						}
            ],
          'initial_options': [
            {
							"text": {
								"type": "plain_text",
								"text": "Bot Impersonations"
							},
							"value": "comments",
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
  
 

