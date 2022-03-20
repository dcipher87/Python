### Reading an entire file

# with open("text_files/pi_digits.txt") as file_object:
#     contents = file_object.read()
# print(contents)


# file_path = "/media/khigha/Windows/Users/khaya/Desktop/Prototype RoboCop/Kickin Book/Coding/Python/Python Crash Course Resources/ehmatthes-pcc_2e-078318e/chapter_10/pi_digits.txt"

# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

### Reading line by line

# file_name = "text_files/pi_digits.txt"

# with open(file_name) as file_object:
#     for line in file_object:
#         #print(line)
#         print(line.rstrip())

### Making a list of lines from a file

# file_name = "pi_digits.txt"

# with open(file_name) as file_object:
#     lines = file_object.readlines()

# #for line in lines:
#     #print(line.rstrip())
# print(lines)

# ### Working with a file's contents
# file_name = "pi_digits.txt"

# with open(file_name) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

### Large files: One million digits
file_name = "pi_million_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]} ...")
print(len(pi_string))

# Is your birthday contained in PI?
birthday = input("Enter your birthday , in the format mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of PI!")
else:
    print("Your birthday does not appear in the first million digits of PI.")
    