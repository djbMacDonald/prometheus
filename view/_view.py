class View:
  
  def __init__(self, request=None, user=None):
    if request:
      self.user = request.get('user_id')
    else:
      self.user = user
    self.external_id = None
    self.private_metadata = None
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
    if self.external_id:
      self.view['external_id'] = f"{self.external_id}_{self.user}"
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
  
  
  