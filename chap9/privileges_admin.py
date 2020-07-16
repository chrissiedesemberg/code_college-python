from chap9.user import User

class Admin(User):

    def __init__(self, first_name, last_name, email, mobile, user_name, *privileges):
        super().__init__(first_name, last_name, email, mobile, user_name)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Your privileges are: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


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