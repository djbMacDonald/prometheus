import random

class RandomUtil:
  
  def rollDice(chanceToSucceed):
    rand = random.random()
    return rand < chanceToSucceed