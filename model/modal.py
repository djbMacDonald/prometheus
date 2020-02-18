class Modal:
  
  def __init__(self, type, req):
    
    self.triggerId = req.get('trrigger_id')
    
    if not self.triggerId:
      return
    
    if type = 'cast':
      caster = Caster()