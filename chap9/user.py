class User:
    """User input capturing"""

    def __init__(self, first_name, last_name, email, mobile, user_name):
        """Initialize name and type attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.user_name = user_name

    def describe_user(self):
        print(f"\nThe user details are:" f"\nFirst name: {self.first_name.title()}"
              f"\nLast Name:  {self.last_name.title()}"
              f"\nEmail:  {self.email.title()}"
              f"\nMobile:  {self.mobile}"
              f"\nuser_name:  {self.user_name.title()}"
              )

    def greet_user(self):
        print(f"\nHi {self.first_name.title()}! Welcome to the platform!")

user_1 = User("mike", "peer", "mike@email", 11937, "mikep")
user_2 = User("susan", "philantro", "suzie@email", 11287, "susie_p")
user_3 = User("arial", "ocean", "swim@email", 11394, "mermaid1")
user_4 = User("gunther", "steed", "guntherthesteed@email", 11934, "batthesteed")