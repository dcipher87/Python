### 5.1 Conditional Tests

# car = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car == "subaru")

# print("Is car == 'audi'? I predict False.")
# print(car == "audi")

# car = "BMW"
# print("Is car == 'bmw'? I predict False")
# print(car == "bmw")

# print("Is car == 'Bmw'? I predict False.")
# print(car == "Bmw")

# print("Is car == 'bmw' if I convert case to lower? I predict True")
# print(car.lower() == "bmw")

# print("Is car == 'BMW'? I predict True.")
# print(car == "BMW")

# Khaya = 34
# print("Is Khaya == 34? I predict True")
# print(Khaya == 34)

# print("Is Khaya over 18? I predict True")
# print(Khaya > 18)

# print("Is Khaya 35? I predict False.")
# print(Khaya == 35)

# print("Is Khaya old enough to retire( at least 55)? I predict False")
# print(Khaya >= 55)

# Khaya = "unemployed"
# print("Is Khaya == 'unemployed'? I predict True")
# print(Khaya == "unemployed")

# print("Is Khaya == 'employed'? I predict False")
# print(Khaya == "employed")

# ### 5.2 More Conditional Tests
# Khaya = "single"
# print("Is Khaya == 'single'? I predict True")
# print(Khaya == "single")

# print("Is Khaya != 'single'? I predict False")
# print(Khaya != "single")

# username = "Khaya"
# print("Is the username == 'khaya'? I predict False")
# print(username == "khaya")

# print("Is the username == 'Khaya'? I predict True")
# print(username == "Khaya")

# print("Is username == 'khaya' if case is lower? I predict True")
# print(username.lower() == "khaya")


# # numerical tests involving equality, inequality, greater than (and equal), less (and equal) or equal to
# teen = 17
# young_adult = 18 # can vote
# adult = 35
# senior_citizen = 56

# print("Can a teen vote?")
# print(teen >= 18)

# print("Can a young adult vote?")
# print(young_adult >= 18)

# print("Can a teen retire?")
# print(teen > 54)

# print("Can a young adult retire?")
# print(young_adult > 54)

# print("Is the adult 35 years old?")
# print(adult == 35)

# print("Is the young adult not 18?")
# print(young_adult != 18)


# print("Is the young adult younger than the teen?")
# print(young_adult < teen)

# print("Is the adult younger than the senior citizen?")
# print(adult < senior_citizen)

# Keywords AND and OR

# AND
# print("Is the adult older than the young adult but younger than the senior citizen?")
# print(adult > young_adult and adult < senior_citizen)

# print("Is the young adult younger than the adult and older than the teen?")
# print(young_adult < adult and young_adult > teen)

# OR
# print("Is senior_citizen older than the adult or the teen?")
# print(senior_citizen > adult or senior_citizen > teen)

# print("Is the adult older than the young adult or older than the senior citizen?")
# print(adult > young_adult or adult > senior_citizen)

# Item IN or NOT IN List
# my_nicknames = ["Khigha", "Kisto", "Enigma", "Strife", "Defjux", "K'", "Kay"]

# print("Is Mango my nickname?")
# print("Mango" in my_nicknames) 

# print("Is Kisto my nickname?")
# print("Kisto" in my_nicknames)

# print("Is Gerald not my nickname?")
# print("Gerald" not in my_nicknames)

### 5.3 Alien Colors #1

# alien_color = "green"
# alien_color = "yellow"
# alien_color = "red"

# # if alien_color == "green":
# #     print("You have just earned 5 points!")

# if alien_color == "red":
#     print("Game over!")

### 5.4 Alien Colors #2

# # alien_color = "green"
# alien_color = "yellow"
# # alien_color = "red"

# if alien_color == "green":
#     print("You have earned 5 points.")
# else:
#     print("You have earned 10 points.")

# alien_color = "green"
# if alien_color == "green":
#     print("You have earned 5 points.")
# else:
#     print("You have earned 10 points.")

# ### 5.5 Alien Colors #3

# alien_color = "green"

# if alien_color == "green":
#     print("You have earned 5 points.")
# elif alien_color == "yellow":
#     print("You have earned 10 points")
# else:
#     print("You have earned 15 points.")

# alien_color = "yellow"

# if alien_color == "green":
#     print("You have earned 5 points.")
# elif alien_color == "yellow":
#     print("You have earned 10 points")
# else:
#     print("You have earned 15 points.")

# alien_color = "red"

# if alien_color == "green":
#     print("You have earned 5 points.")
# elif alien_color == "yellow":
#     print("You have earned 10 points")
# else:
#     print("You have earned 15 points.")

# ### 5.6 Stages of Life

# # age = 21
# ages = [1, 2, 4, 13, 20, 65]

# for age in ages:
#     if age < 2:
#         print("You are a baby.")
#     elif age < 4:
#         print("You are a toddler.")
#     elif age < 13:
#         print("You are a kid.")
#     elif age < 20:
#         print("You are a teenager.")
#     elif age < 65:
#         print("You are an adult.")
#     else:
#         print("You are an elder.")

### 5.7 Favourite Fruit

# favourite_fruits = ["apple", "banana", "peach", "watermelon", "orange"]

# apple, pear, pinapple, naartjie, kiwi, pawpaw

# if "apple" in favourite_fruits:
#     print("You really like apples!")
# if "pear" in favourite_fruits:
#     print("You really like pears!")
# if "naartjie" in favourite_fruits:
#     print("You really like naartjies!")
# if "orange" in favourite_fruits:
#     print("You really like oranges!")
# if "kiwi" in favourite_fruits:
#     print("You really like kiwis!")

# fruits = ["apple", "pear", "watermelon", "banana", "pinapple", "naartjie", "kiwi", "pawpaw"]

# for fruit in fruits:
#     if fruit in favourite_fruits:
#         print(f"You really like {fruit}s!")

### 5.8 Hello Admin

# usernames = ["Khaya", "Dcipher", "Khigha", "admin", "Kisto", "Strife", "DefJux"]

# for name in usernames:
#     if name == "admin":
#         print(f"Hello {name.title()}, would you like to see a status report?")
#     else:
#         print(f"Hello {name.title()}, thank you for logging in again!")

# ### 5.9 No Users

# # usernames = ["Khaya", "Dcipher", "Khigha", "admin", "Kisto", "Strife", "DefJux"]

# usernames = []

# if usernames:
#     for name in usernames:
#         if name == "admin":
#             print(f"Hello {name.title()}, would you like to see a status report?")
#         else:
#             print(f"Hello {name.title()}, thank you for logging in again!")
# else:
#     print("We need to find some users!")

# ### 5.10 Checking Usernames

# users_current = ["Khaya", "Dcipher", "Khigha", "admin", "Kisto", "Strife", "DefJux"]

# current_users = []

# # append lowercase usernames into new list for duplicate check
# for user in users_current:
#     lower_user = user.lower()
#     current_users.append(lower_user)

# #print(current_users)

# new_users = ["Cairo", "Berlin", "Khigha", "Nairobi", "London", "Rio", "Durban", "DefJux"]
# # new_users = []

# if new_users:
#     for user in new_users:
#         if user.lower() in current_users:
#             print(f"{user.title()} is not available. Please enter a new username.")
#         else:
#             print(f"Username {user.title()} is avaialble.")
# else:
#     print("There are no new users.")

# ### 5.11 Ordinal Numbers

# numbers = list(range(1,10))
# #print(numbers)

# for number in numbers:
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")
#     else:
#         print(f"{number}th")
