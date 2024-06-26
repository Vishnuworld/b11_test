from .constant import USERNAME, PASSWORD


def login(user, password):
    "user login"
    if user == USERNAME and password == PASSWORD:
        print("user logged in successfully.")
    else:
        print("Invalid credentials.")

def logout():
    print("logout")



def register(user, pswd, email, mob):
    print("Registered 1000 lines.")
