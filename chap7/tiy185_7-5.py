# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s
# age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is
# $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
# and then tell them the cost of their movie ticket.


age = input("\nHow old are you?")
age = int(age)
print(f"\nYou are {age} years old.")

if age < 3:
    print("Your ticket for the movie will be free of charge")
elif age < 12:
    print("Your ticket for the movie will cost R10.00")
else:
    print("Your ticket for the movie will cost R15.00")




