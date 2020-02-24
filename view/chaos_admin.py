from view._view import View

class ChaosAdminView(View):
  
  def __init__(self, user):
    super().__init__(user)    
  
    
  def build(self):
    self.setTitle('Chaos Admin')    
    self._finalize()
    return self.view
  
 

