users = ["John", "Angie", "Susan", "Cliff"]
for user in users:
    if user in users:
        print(f"Welcome {user}!")

users.remove("John")
users.remove("Angie")
users.remove("Susan")
users.remove("Cliff")

for user in users:
    if user in users:
        print(f"Welcome {user}!")
    else:
        print("We need to find some users!")
    continue