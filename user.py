class User:
    registered_users = dict()

    def __init__(self, user_id=None, username=None, email=None, password=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def register(self,username,email,password):
        if username in User.registered_users:
            return "User already exits. Proceed to Login"
        else:
            User.registered_users[username] = {
                "userID": len(User.registered_users) + 1,
                "email": email,
                "password": password
            }
            return "Registration successful. You can now login"
    
    def login(self,username,password):
        if username in User.registered_users:
            if password == User.registered_users[username]["password"]:
                print("Login Successful")
                return "Login Successful"
            else:
                return "Incorrect Password. Please try again"
        else: return "Username not found!! Register user"

user = User()
print(user.registered_users)

# Register new users and display registration/login messages
print(user.register("alice", "alice@example.com", "password123"))
print(user.register("bob", "bob@example.com", "pass456"))
print(user.login("alice", "password123"))
print(user.login("bob", "wrongpassword"))
print(user.login("carol", "somepassword"))
 