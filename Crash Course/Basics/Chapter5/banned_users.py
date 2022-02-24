## Check whether a value is not in a list (using NOT)

banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

user = "carolina"
if user in banned_users:
    print(f"{user.title()} is banned and cannot post a response.")

if user not in banned_users:
    print(f"{user.title()}, you can post a response.")
else:
    print(f"{user.title()} you are banned and cannot post a response")