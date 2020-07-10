filename = "python_lessons.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    if "Python" in line:
        print(line.replace("Python", "Java"))



