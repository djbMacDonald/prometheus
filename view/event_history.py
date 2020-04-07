from view._view import View


class EventHistoryView(View):
  
  def build(self):
    self.setTitle('Event History, most recent on top')    
    self._buildHistory()  
    self._finalize()
    return self.view
  
  def _buildHistory(self):
    # events = "\n".join(open('event_log.txt', 'r').read().splitlines()[-20:])
    # eventsMessage = "\n".join(events)
    self._blocks.append(
        { 
           "type":"section",
           "text":{ 
              "type":"mrkdwn",
              "text": text
           }
        }
      )