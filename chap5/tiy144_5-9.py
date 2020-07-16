users = ["John", "Angie", "Susan", "Cliff"]
print(users)

while len(users) > 0:
    for user in users:
        print(f"Welcome {user}!")
        users.remove(user)
else:
    print("\nWe have now removed all users")
    print(f"We need to find some users!")

