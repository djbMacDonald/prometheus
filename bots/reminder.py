from utils.post import PostUtil
import random
from model.identity import Identity
import requests
from constant.channels import CHANNELS

class ReminderBot:
  
  @classmethod
  def description(cls):
    return "`Name bot` ".format()
  
  def __init__(self, eventModel, pool):
    self._event = eventModel
    self._postUtil = PostUtil(pool)
  
  def run(self):
    if not self._event.event() or not self._event.isFromABot() or not self._event.isInChannel('Reminders') or not self._event.isFromBot('reminder') or not self._event.text() == 'Reminder: Trigger Schemes Poll.':
      return
    
    dayOffset = 3
    now = datetime.datetime.now()
    monday = now + datetime.timedelta(days=dayOffset)
    tuesday = now + datetime.timedelta(days=dayOffset+1)
    wednesday = now + datetime.timedelta(days=dayOffset+2)
    thursday = now + datetime.timedelta(days=dayOffset+3)
    friday = now + datetime.timedelta(days=dayOffset+4)
  
    pollText = '"Game Planning: Week Of {}/{}" "Monday {}/{}" "Tuesday {}/{}" "Wednesday {}/{}" "Thursday {}/{}" "Friday {}/{}"'.format(
      monday.month,
      monday.day, 
      monday.month, 
      monday.day,
      tuesday.month, 
      tuesday.day, 
      wednesday.month,
      wednesday.day,
      thursday.month, 
      thursday.day, 
      friday.month, 
      friday.day
    )
    self._postUtil.useCommand('/polly', pollText, CHANNELS['Schemes'])