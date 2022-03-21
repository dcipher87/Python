### 10.1 Learning Python

# file_name = "learning_python.txt"

# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents)

# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.strip())

# with open(file_name) as file_object:
#     lines = file_object.readlines()

# print(lines)
# for line in lines:
#     print(line)

# ### 10.2 Learning C

# file_name = "learning_python.txt"

# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.replace("Python", "JavaScript"))


# ### 10.3 Guest

# guest_name = input("Enter your name: ")

# file_name = "guest.txt"

# with open(file_name, 'w') as file_object:
#     file_object.write(guest_name)

# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents)

# ### 10.4 Guest book

# active = True
# file_name = "guest_book.txt"

# prompt = "Enter your name: "
# prompt += "Type 'q' anytime to quit. "

# with open(file_name, 'w') as file_object:
#     file_object.write("The following people visited our site today: \n")

# while active:
#     guest = input(prompt)
#     if guest == 'q':
#        active = False
#     else:
#         print(f"Hi {guest.title()}, thanks for visiting our site!\n")
#         with open(file_name, 'a') as file_object:
#             file_object.write(f"\t - {guest}\n")

# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents)

# ### 10.5 Programming Poll

# active = True
# file_name = "programming.txt"

# with open(file_name, 'w') as file_object:
#     file_object.write("Some reasons people love programming: \n")

# prompt = "Tell us why you love programming. "
# prompt += "Enter 'q' anytime to quit. "

# while active:
#     phrase = input(prompt)
#     if phrase == 'q':
#         active = False
#     else:
#         with open(file_name, 'a') as file_object:
#             file_object.write(f"\t - {phrase}\n")

# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents)

# ### 10.6 Addition

# prompt = "Give me two numbers and I will give you their sum: "
# prompt += "Enter 'q' anytime to quit."
# print(prompt)

# first_number = input("First number: ")
# second_number = input("Second number: ")
# try:
#     answer = int(first_number) + int(second_number)
# except ValueError:
#     print("I can only add numbers! Please provide an integer.")
# else:
#     print(answer)


# ### 10.7 Addition Calculator
# def sum_numbers():
#     """Finds the sum of two numbers received from user."""
#     prompt = "Give me two numbers and I will give you their sum: "
#     prompt += "Enter 'q' anytime to quit."
#     print(prompt)

#     while True:
#         first_number = input("First number: ")
#         if first_number == 'q':
#             break
#         second_number = input("Second number: ")
#         if second_number == 'q':
#             break
#         try:
#             answer = int(first_number) + int(second_number)
#         except ValueError:
#             print("I can only add numbers! Please provide an integer.")
#         else:
#             print(answer)

# sum_numbers()

# ### 10.8 Cats and Dogs

# #file_name = "cats.txt" 
# file_name = "dogs.txt"
# #file_name = "iguanas.txt"

# try:
#     with open(file_name) as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"The file {file_name} cannot be found.")
# else:
#     print(contents)

# files = ["cats.txt", "dogs.txt", "iguanas.txt"]

# for file in files:
#     try:
#         with open(file) as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"The file {file} cannot be found.")
#     else:
#         print(contents)

# ### 10.9 Silent Cats and Dogs

# files = ["cats.txt", "dogs.txt", "iguanas.txt"]

# for file in files:
#     try:
#         with open(file) as f:
#             contents = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         print(contents)

# ### 10.10 Common Words

# file_name = "alice.txt"

# with open(file_name) as f:
#     contents = f.read()

# # alice_count = contents.lower().count("alice")
# # print(alice_count)

# the_count = contents.lower().count("the")
# print(the_count)

# the_count = contents.lower().count("the ")
# print(the_count)

# ### 10.11 Favourite Number

# import json

# file_name = "favourite_number.json"

# # with open(file_name, 'w') as f:
# #     favourite_number = input("What is your favourite number? ")
# #     json.dump(favourite_number, f)

# # with open(file_name) as f:
# #     favourite_number = json.load(f) #f.read()
# #     print(f"I know your favourite number is {favourite_number}!")

# ### 10.12 Favourite Number Remembered
# import json

# file_name = "favourite_number.json"

# try:
#     with open(file_name) as f:
#         favourite_number = json.load(f)
#         print(f"Your favourite number is {favourite_number}!")
# except FileNotFoundError:
#     favourite_number = input("What is your favourite number? ")
#     with open(file_name, 'w') as f:
#         json.dump(favourite_number, f)
#         print(f"We'll remember that your favourite number is {favourite_number}!")

# ### 10.13 Verify User
# import json

# def get_stored_username():
#     """Get stored username if available."""
#     file_name = "username.json"
#     try:
#         with open(file_name) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def get_new_username():
#     """Prompts user for username and stores it."""
#     username = input("What is your name? ")
#     file_name = "username.json"
#     with open(file_name, 'w') as f:
#         json.dump(username, f)
#         return username 

# def greet_user():
#     """Greet user by name."""
#     username = get_stored_username()
#     if username:
#         verify = input(f"Hello there, are you {username}? (Y/N)")
#         verify.lower()
#         if verify == 'y':
#             print(f"Welcome back, {username.title()}!")
#         else:
#             username = get_new_username()
#             print(f"We'll remember you when you come back {username.title()}!")
#     else:
#        username = get_new_username()
#        print(f"We'll remember you when you come back {username.title()}!")

# greet_user()