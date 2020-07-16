from chap9.tiy229_9_3 import User

class Admin(User):

    def __init__(self, first_name, last_name, email, mobile, user_name, *privileges):
        super().__init__(first_name, last_name, email, mobile, user_name)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Your privileges are: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


#administrator = Admin("John", "Doe", "email@email", "0716784503", "jhnd","can add post", "can delete post", "can ban user")
#administrator.describe_user()
#administrator.show_privileges()