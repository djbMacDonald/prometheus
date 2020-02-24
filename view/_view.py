class View:
  
  def __init__(self, user=None, view=None, state=None):
    self.user = user.user
    self.external_id = None
    self.private_metadata = None
    self._blocks = []
    self._header = {"type": "modal"}
    self.setTitle('Sample Modal')
    self.view = view
    self.state =

    
    
  def build(self):
    self.setSubmit('Submit')
    self.setClose('Cancel')
    self._finalize()
    return self.view
    
    
  def _finalize(self):
    self.view = self._header
    if self.external_id and self.user.id:
      self.view['external_id'] = f"{self.external_id}_{self.user.id}"
    if self.private_metadata:
      self.view['private_metadata'] = self.private_metadata
    self.view['blocks'] = self._blocks
    
    return self.view
  
  def setSubmit(self, text):
    self._header['submit'] = {
      "type": "plain_text",
      "text": text,
      "emoji": True,
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
  
  
  