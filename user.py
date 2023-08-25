import hashlib, random

class User:
    registered_users = dict()
    user_id_counter = 1

    def __init__(self, username, email,password):
        self.user_id = User.user_id_counter
        self.username = username
        self.email = email
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        User.registered_users[username] = self
        User.user_id_counter += 1

    def verify_password(self,password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def register(cls,username,email,password):
        if username in cls.registered_users:
            return "User already exits. Proceed to Login"
        else:
            new_user = cls(username,email,password)
            # User.registered_users[username] = {
            #     "userID": len(User.registered_users) + 1,
            #     "email": email,
            #     "password": password
            # }
            return "Registration successful. You can now login"
    
    @classmethod
    def login(cls,username,password):
        if username in cls.registered_users:
            user = cls.registered_users[username]
            if user.verify_password(password):
                return True,user,"Login Successful"
            else:
                return "Incorrect Password. Please try again"
        else: return "Username not found!! Register user"


# # Register new users and display registration/login messages
# print(User.register("alice", "alice@example.com", "password123"))
# print(User.register("bob", "bob@example.com", "pass456"))
# print(User.login("alice", "password123"))
# print(User.login("bob", "wrongpassword"))
# print(User.login("carol", "somepassword"))
 