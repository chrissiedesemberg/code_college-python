from chap9.tiy242_9_8 import Privileges
from chap9.tiy242_9_7 import Admin

print(f"\n\n\n New user coming in: \n")
new = Admin("Firstname", "Lastname", "emailaddress", 111111, "tiktok")

new.describe_user()
new.show_privileges()
new_privileges = [
    "do magic",
    "disappear",
    "know everything"
]

new.privileges = new_privileges
new.show_privileges()