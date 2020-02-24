from view._view import View

class ChaosView(View):
  
  def __init__(self, req, user):
    super().__init__(req)
    
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
								"text": "New tasks"
							},
							"value": "tasks",
							"description": {
								"type": "plain_text",
								"text": "I would like to recieve notifications in active threads"
							}
						},
						{
							"text": {
								"type": "plain_text",
								"text": "New comments"
							},
							"value": "comments",
							"description": {
								"type": "plain_text",
								"text": "I would like to be eligibile for a bot impersonation"
							}
						}
            ],
          'initial_options': [
            "tasks"
          ]
          }
        ]
      }
    )
    return
  
 

