class View:
  
  def __init__(self, request):
    self.user = request.get('user_id')
    self._blocks = []
    self._header = {"type": "modal"}
    self.setTitle('Sample Modal')

    
    
  def build(self):
    self.setSubmit('Submit')
    self.setClose('Cancel')
    self._finalize()
    return self.view
    
    
  def _finalize(self):
    self.view = self._header
    if self.id:
      self.external_id
    self.view['blocks'] = self._blocks
    return self.view
  
  def setSubmit(self, text):
    self._header['submit'] = {
      "type": "plain_text",
      "text": text,
      "emoji": True
    }
    return
    
  def setClose(self, text):
    self._header['close'] = { 
      "type":"plain_text",
      "text": text,
      "emoji":True
    }
    return
  
  def setTitle(self, text):
    self._header['title'] = {
      "type":"plain_text",
      "text": text,
      "emoji":True
    }
    return
  
  
  