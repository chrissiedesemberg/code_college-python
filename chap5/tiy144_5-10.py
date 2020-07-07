current_users = ["Gabriel", "Michael", "Susan", "Rachel", "Guy"]
new_users = ["jane", "tarzan", "william", "gabriel", "michael"]

for new in new_users:
    if new.title() in current_users:
        print(f"This username {new} has already been taken. Please enter a new username.")
    else:
        print(f"The username {new} is still available")