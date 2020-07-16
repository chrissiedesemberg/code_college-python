

from random import randint


class Die:
    """ create different sides die"""
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        rolled = randint(1, self.sides)
        return rolled

#6 sided dice
results6 = []
side_6 = Die(6)
for roll in range(10):
    answer = side_6.roll_die()
    results6.append(answer)
print("\nThe 6 sided dice rolled for 10 times:")
print(results6)

#10 sided dice
results10 = []
side_10 = Die(10)
for roll in range(10):
    answer = side_10.roll_die()
    results10.append(answer)
print("\nThe 10 sided dice rolled for 10 times:")
print(results10)

#20 sided dice
results20 = []
side_20 = Die(20)
for roll in range(10):
    answer = side_20.roll_die()
    results20.append(answer)
print("\nThe 20 sided dice rolled for 10 times:")
print(results20)