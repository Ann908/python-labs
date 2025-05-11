import hashlib
class User:
    def __init__(self, username, password_hash, is_active):
        self.username = username
        self.password_hash = hashlib.md5(password_hash.encode()).hexdigest()
        self.is_active = is_active

    def verify_password(self, password):
        password = hashlib.md5(password.encode()).hexdigest()
        if password == self.password_hash:
            return True
        else:
            return False

#my_user = User('ani', 'password', True)
#print(my_user.username)

class Administrator(User):
    def __init__(self, username, password_hash, is_active):
        super().__init__(username, password_hash, is_active)
        self.list_permission = ['allowed', 'forbidden', 'partially allowed']

    def printing_permissions(self):
        print(f"Administrator has the following permissions {self.list_permission}")

class RegularUser(User):
    def __init__(self, username, password_hash, is_active, last_login_date):
        super().__init__(username, password_hash, is_active)
        self.last_login_date = last_login_date

#my_u = RegularUser('ani', 'password', True, '20.04.2025')
#print(my_u.last_login_date)

class GuestUser(User):
    def __init__(self, username, password_hash='', is_active=False):
        super().__init__(username, password_hash, is_active)

    def verify_password(self, password):
        return False

class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password) and user.is_active:
            return user
        else:
            return None

if __name__ == "__main__":
    admin = Administrator("admin", "admin123", True)
    user1 = RegularUser("user1", "mypassword", True, "11.05.2025")
    guest = GuestUser("guest")  #automatic password '' і is_active=False
    inactive_user = RegularUser("inactive", "inactivepass", False, "10.05.2025")

    #Adding users in system
    user_control = AccessControl()
    user_control.add_user(admin)
    user_control.add_user(user1)
    user_control.add_user(inactive_user)

    #Authication user in system
    authenticated_user = user_control.authenticate_user("user1", "mypassword")
    if authenticated_user:
        print(f"Login is successful: {authenticated_user.username}")
    else:
        print("Failed login attempt.")

    authenticated_user2 = user_control.authenticate_user("inactive_user", "pass123456")
    if authenticated_user2:
        print(f"Login is successful: {authenticated_user.username}")
    else:
        print("Failed login attempt.")


