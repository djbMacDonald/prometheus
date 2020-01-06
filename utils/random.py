import random

#move to static functions
class Random:
  
  def rollDice(self, chanceToSucceed):
    rand = random.random()
    return rand < chanceToSucceed