#Stripping Names: Use a variable to represent a person’s name, and include some
#whitespace characters at the beginning and end of the name. Make sure you use each character
#combination, "\t" and "\n", at least once.
#Print the name once, so the whitespace around the name is displayed. Then print the name
#using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "Here is the name on the next line \nTodd";
print(name)

name = "Todd"
print(name)

name = "\tTodd\t";
print(name)
print(name.lstrip())
print(name.rstrip())

name = "\tTodd\t";
print(name)
print(name.strip())




