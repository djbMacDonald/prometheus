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
    
    return
  
 

