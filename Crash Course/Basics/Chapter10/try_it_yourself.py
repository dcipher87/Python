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
