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
