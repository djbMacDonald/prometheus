class View:
  
  def __init__(self, request):
    self.user = request.get('user_id')
    self._blocks = []
    self._header = {"type": "modal"}
    
    
  def _finalize(self):
    self.view = self._header
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
  
  
  