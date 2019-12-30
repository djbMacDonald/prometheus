from constant.settings import DEBUG

class LogUtil:
  
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