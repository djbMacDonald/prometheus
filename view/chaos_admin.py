from view._view import View

class ChaosAdminView(View):
  
  def __init__(self, req, user):
    super().__init__(req)    
  
    
  def build(self):
    self.setTitle('Chaos Admin')    
    self._finalize()
    return self.view
  
 

