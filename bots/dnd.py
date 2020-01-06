import random
from model.identity import Identity
import requests
import json
from bots.bot import Bot

class Dnd(Bot):
  
  def run(self):
    if self._event.isFromABot() or not self._event.text() or not self._event.text()[0] == '!':
      return
    
    command = self._event.text()[1:].split()
    if command[0] == 'class':
      url = 'http://www.dnd5eapi.co/api/classes/{}'.format(command[1]);
      response = json.loads(requests.get(url).content)
      if not response:
        return
      responseMessage = '*{}*\n'.format(response['name'])
      responseMessage += '>Proficiencies:\n>```';
      for prof in response['proficiencies']:
        responseMessage += '{}\n'.format(prof['name'])
      responseMessage += '```\n\n'
      
      responseMessage += '>Proficiency Choices ({}):\n>```'.format(response['proficiency_choices'][0]['choose']);
      for prof in response['proficiency_choices'][0]['from']:
        responseMessage += '{}\n'.format(prof['name'])
      responseMessage += '```\n\n'
      
      responseMessage += '>Proficiency Choices ({}):\n>```'.format(response['proficiency_choices'][0]['choose']);
      for prof in response['proficiency_choices'][0]['from']:
        responseMessage += '{}\n'.format(prof['name'])
      responseMessage += '```\n\n'
    
      responseMessage += '>Saving Throws:\n>```';
      for prof in response['saving_throws']:
        responseMessage += '{}\n'.format(prof['name'])
      responseMessage += '```\n\n'    
  
      responseMessage += '>Subclasses:\n>```';
      for prof in response['subclasses']:
        responseMessage += '{}\n'.format(prof['name'])
      responseMessage += '```\n\n'
      
      self._postUtil.addMessage(responseMessage, self._event.channel(), self._event.threadId())