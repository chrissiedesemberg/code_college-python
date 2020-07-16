from chap9.tiy242_9_7 import Admin

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Your privileges are: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("You have no privileges")

admininistrator = Admin("Chrissie", "Desemberg", "email@", 7167894539, "lella")
admininistrator.describe_user()
admininistrator.show_privileges()

admininistrator_privileges = [
    "can add users",
    "can delete users"
]
admininistrator.privileges = admininistrator_privileges
admininistrator.show_privileges()
