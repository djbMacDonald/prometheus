from model.caster import Caster

class Modal:
  def __init__(self, type, req):
    
    self.triggerId = req.get('trrigger_id')
    self.header = {"type": "modal"}
    
    
    if not self.triggerId:
      return
    
    if type == 'cast':
      caster = Caster(req.get('user_id'))
      self.setSubmit('Cast')
      self.setClose('Cancel')
      self.setTitle(Caster.name)
      self.setView = Caster.getCastingView()
      
      
  def open(self):
    if not self.view:
      
      return
  
  def setSubmit(self, text):
    self.header['submit'] = {
          "type": "plain_text",
          "text": text,
          "emoji": True
     }
    return
    
  def setClose(self, text):
    elf.header['close'] = { 
          "type":"plain_text",
          "text": text,
          "emoji":True
       }
    return
  
  def setTitle(self, text):
    self.header['title'] = {
      { 
          "type":"plain_text",
          "text": text,
          "emoji":True
       }
    }
    return
  
  def setView(self, view):
    self.view = self.header
    self.view['blocks'] = view