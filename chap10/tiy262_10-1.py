filename = 'python_lessons.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

file = ""

for line in lines:
    file += line

print(f"{file}")