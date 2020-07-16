current_users = ["Gabriel", "Michael", "Susan", "Rachel", "Guy"]
new_users = ["jane", "tarzan", "william", "gabriel", "michael"]

for username in new_users:
    if username.title() in current_users:
        print(f"This username {username} has already been taken. Please enter a new username.")
    else:
        print(f"The username {username} is still available")