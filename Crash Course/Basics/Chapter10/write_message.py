file_name = "programming.txt"

# with open(file_name, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")

# with open(file_name) as file_object:
#     contents = file_object.read()

# print(contents)

with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that run in a browser.\n")

with open(file_name) as file_object:
    for line in file_object:
        print(line)
