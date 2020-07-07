print("EXAMPLE 1 & 2")
result = "passed"
print("Is result == 'passed'? I predict true")
print(result == "passed")

print("Is result == 'failed'? I predict false")
print(result == "failed")

print("\nEXAMPLE 3 & 4")
pet = "DOG"
print(pet.lower() == "dog") #true
print(pet.lower() == "cat") #false

print("\nEXAMPLE 5")
fruits = ["pear", "apple", "oranges", "apricots"]
print("pear" in fruits or "strawberries" in fruits) #true

print("\nEXAMPLE 6")
username = "Alias"
email = "Address"
if username.upper() == "ALIAS" and email.lower() == "address":
    print("We have you in our database")
print(username.upper() == "ALIAS" and email.lower() == "address") #true

print("\nEXAMPLE 7")
username = "twinninghard"
password = "chocchipcookieswins14"
print(username == "twinninghard" and password == "chocchipcookieswins143") #false

print("\nEXAMPLE 8")
toddler_age_1 = "under 12 months"
toddler_age_2 = "over 12 months"
toddler_milk_1 = "formula"
toddler_milk_2 = "cow milk"
print(toddler_age_1 == "under 12 months" or toddler_milk_1 == "cow milk") #true
print(toddler_age_1 == "under 12 months" and toddler_milk_1 == "cow milk") #false
print(toddler_age_1 == "under 12 months" and toddler_milk_2 == "cow milk") #true

print("\nEXAMPLE 9 & 10")
age_1 = 12
age_2 = 4
print(age_1 >= 10 and age_2 <= 10) #true
print(age_1 <= 10 and age_2 <= 10) #false
