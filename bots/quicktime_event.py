import random
from model.identity import Identity
from constant.language import VOWELS
from constant.people import USERS, IDENTITIES
from bots._bot import Bot

class Pig(Bot):
  
  
  # @classmethod
  # def description(cls):
  #   return "`Pig` Has a {}% chance of replacing {}'s message with pig latin".format(cls._frequency * 100, cls._target)
  
  def run(self):
    return