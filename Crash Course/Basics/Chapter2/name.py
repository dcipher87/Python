# Exercse to illustrate inclusion and removal of white spaces

# name = "khaya ubisi"
# print(name.title())
# print(name.upper())


# name = "KHAYA UBISI"
# print(name.lower())

# first_name = "khaya"
# last_name = "ubisi"
# full_name = first_name + " " + last_name

# # print(full_name.title())
# message = "Hello, " + full_name.title() + "!"
# print(message)

# print("Python")
# print("\tPython")
# print("\n")


# print("Languages: \nPython\nC\nJavaScript")
# print("\n")

# print("Languages: \n\tPython \n\tC \n\tJavaScript")

###################################################
# Stripping whitespace
# favourite_language = "python "
# print(favourite_language)
# print(favourite_language.rstrip()) #rstript() removes trailing whitespace temporarily

# favourite_language = favourite_language.rstrip()
# print(favourite_language)

favourite_language = "  python  "
favourite_language.rstrip() # removes whitespace to the right of text
favourite_language.lstrip() # removes whitespace to the left of text
favourite_language.strip() # removes whitespace on either side of text