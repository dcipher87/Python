# import json

# username = input("What is your name: ").lower()

# file_name = "username.json"
# with open(file_name, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username.title()}!")

import json
 
#Load the username, if previously stored
#Otherwise, prompt for username and store it

# def greet_user():
#     """Greets existing user by name or stores new user name and greets."""
#     file_name = "usernames.json"

#     try:
#         with open(file_name) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(file_name, 'w') as f:
#             json.dump(username, f)
#             print(f"We'll remember you when you come back, {username.title()}!")
#     else:
#         print(f"Welcome back, {username.title()}")


### Refactoring

def get_stored_username():
    """Get stored username if available."""
    file_name = "username.json"
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompts user for username and stores it."""
    username = input("What is your name? ")
    file_name = "username.json"
    with open(file_name, 'w') as f:
        json.dump(username, f)
        return username 

def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
       username = get_new_username()
       print(f"We'll remember you when you come back {username.title()}!")

greet_user()
    