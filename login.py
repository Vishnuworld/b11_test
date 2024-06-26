from .constant import USERNAME, PASSWORD


def login(user, password):
    "user login"
    if user == USERNAME and password == PASSWORD:
        print("user logged in successfully.")
    else:
        print("Invalid credentials.")
