USERNAME = "ADMIN"
PASSWORD = "admin123"


def login(user, password):
    if user == USERNAME and password == PASSWORD:
        print("user logged in successfully.")
    else:
        print("Invalid credentials.")
