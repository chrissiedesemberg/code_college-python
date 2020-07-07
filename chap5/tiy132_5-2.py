print("\nEXAMPLE 1")
dog = "Boston Terrier"
color = "Bridle"
if dog.lower() == "boston terrier" and color.lower() == "bridle":
    print("You have my favorite dog, a brown Bostie!")
else:
    print("Your dog is definitely not as smart as smart or pretty as mine!")
print(color.lower() == "bridle") #true
print(color.upper() == "bridle") #false

print("\nEXAMPLE 2")
height = 1.74
weight = 80
sex = "male"
if height >= 1.64 and weight <= 70 and sex.lower() == "female":
    print("Keep up the good work - you are not overweight!")
elif height <= 1.74 and weight >= 70 and sex == "female":
    print("Get to gym asap!")
else:
    print("We don't have the numbers for men!")
print(height >= 1.60 and weight <= 60)  #false
print(height >= 1.60 or weight <= 60)  #true
print(height == 1.74 and weight >= 60)  #true
height = "1.74"
print(height == 1.74) #false
