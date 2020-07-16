from chap9.user import User
from chap9.privileges_admin import Privileges, Admin

new_admin = Admin("Final", "Test", "email", 98765, "user_test", "can be tested", "works all around", "this was easy?")
new_admin.describe_user()
new_admin.show_privileges()