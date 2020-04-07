from view._view import View


class EventHistoryView(View):
  
  def build(self):
    self.setTitle('Events, recent on top')    
    self._buildHistory()
    self._finalize()
    return self.view
  
  def _buildHistory(self):
    events = open('event_log.txt', 'r').read().splitlines()[-20:]
    events.reverse()
    self._blocks.append(
      { 
         "type":"section",
         "text":{ 
            "type":"mrkdwn",
            "text": "\n".join(events)
         }
      }
    )