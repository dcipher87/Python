# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# language = favourite_languages['sarah'].title()
# print(f"Sarah's favourite language is {language}.")

# Looping through key value pairs in dictionary
# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# # for key, value in favourite_languages.items():
# for name, language in favourite_languages.items():
#     # print(f"\nName: {key.title()}")
#     # print(f"Favourite Language: {value.title()}")
#     print(f"{name.title()}'s favourite language is {language.title()}.")

# # Looping through all the Keys in a dictionary
# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# print("The following people took the poll:")
# for name in favourite_languages.keys():
#     print(name.title())

# # for name in favourite_languages:
# #     print(name)

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# friends = ['phil', 'sarah']

# for name in favourite_languages.keys():
#     print(f"Hi {name.title()}")

#     if name in friends:
#         language = favourite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# # Using the keys() method to find if an item is a key in a dictionary

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# if 'erin' not in favourite_languages.keys():
#     print("Erin, please take our poll!")

# ### Looping through a dictionary's keys in a particular order
# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# # for name in sorted(favourite_languages.keys(), reverse=True):
# #     print(f"{name.title()}, thank you for taking the poll.")
# # # sorted() makes alphabetical a - z, reversed() makes original order in reverse, sorted(, reverse=True) makes z - a

# for name, language in sorted(favourite_languages.items()):
#     print(f"{name.title()}, thank you for taking my poll and confirming that {language.title()} is your favourite programming language.")

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# print("The following languages have been mentioned in the poll:")
# for language in favourite_languages.values():
#     print(f"{language.title()}")
# # values() method returns the values without the keys, this method will return each value including duplicates (python appears twice)

# # to exclude duplicates use the set() method, a set is a collection of unique items
# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# print("The following languages have been mentioned in the poll:")
# for language in set(favourite_languages.values()):
#     print(f"{language.title()}")

# a set is a list with curly braces but no key-value pairs
languages = {'python', 'ruby', 'python', 'c'}
print(languages)