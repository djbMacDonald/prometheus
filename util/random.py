import random

class RandomUtil:

  def rollDice(self, chanceToSucceed):
    rand = random.random()
    return rand < chanceToSucceed