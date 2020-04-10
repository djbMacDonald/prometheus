class ActionQueue:
  
  _replacements = []
  _replies = []
  _reactions = []
  
  def __init__(self, pool):
    self._log = Log()
    self._pool = pool
  
  def shouldDelete():
    return
  
  def replacement(self):
    return
  
  def replies(self):
    return
  
  def addReaction(self, bot, channel, reaction):
    self._reactions.append(
      {'bot': bot, "channel": channel, 'reaction': reaction}
    )
    return
  
  def reactions(self):
    return
  
  def flush(self):
    return