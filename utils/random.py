import random

#move to static functions
class RandomUtil:
  
  def rollDice(self, chanceToSucceed):
    rand = random.random()
    return rand < chanceToSucceed