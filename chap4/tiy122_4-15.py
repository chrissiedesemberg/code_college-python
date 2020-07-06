#1
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friends_food in friend_foods:
    print(friends_food)

#2
numbers = range(3, 30, 3)
for threes in numbers:
    print(threes)

#3
cubes = []
for number in range(1, 10):
    cube = number**3
    cubes.append(cube)
print(cubes)

print("\nThe three first items in the list are:")
print(cubes[0:3])

print("\nThree items from the middle of the list are:")
print(cubes[3:6])

print("\nThe last three items in the list are:")
print(cubes[-3:])