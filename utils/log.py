from constant.settings import DEBUG

#move to static functions
class Log:
  
  def logEvent(self, eventMessage):
    f = open('event_log.txt', 'a+')
    f.write('{}\r\n'.format(eventMessage))
    f.close()
    print(eventMessage)
      
  def logToFile(self, event):
    f = open('{}_logfile.txt'.format(event.channel()), 'a+')
    f.write('{}\r\n'.format(event.text()))
    f.close()
    if DEBUG:
      self._printFile()

def logToNewFile(self, event):
  f = open('{}_logfile.txt'.format(event.channel()), 'w+')
  f.write('{}\r\n'.format(event.text().encode('utf-8')))
  self._printFile()  

def _printFile(self, event):
  print('reading file')
  f = open('{}_logfile.txt'.format(event.channel()), 'r').read().splitlines()
  for line in f:
    print(line)