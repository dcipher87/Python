### 6.1 Person

# person = {
#     'first_name': 'khaya',
#     'last_name': 'ubisi',
#     'age': 34,
#     'city': 'johannesburg',
# }
# print(person['first_name'].title())
# print(person['last_name'].title())
# print(person['age'])
# print(person['city'].title())

# ### 6.2 Favourite Numbers

# favourite_numbers = {
#     'khaya': 13,
#     'khigha': 7,
#     'defjux': 34,
#     'strife': 144,
#     'enigma': 9,
#     }

# print(f"Khaya's favourite number is {favourite_numbers['khaya']}.")
# print(f"Khigha's favourite number is {favourite_numbers['khigha']}.")
# print(f"DefJux's favourite number is {favourite_numbers['defjux']}.")
# print(f"Strife's favourite number is {favourite_numbers['strife']}.")
# print(f"Enigma's favourite number is {favourite_numbers['enigma']}.")

# ### 6.3 Glossary

# glossary = {
#     'variable': 'data values that can change',
#     'loop': 'sequence of instructions that is continually repeated',
#     'range': 'set of possible values a variable can hold',
#     'slice': 'a subset of data values in a dataset',
#     'tuple': 'an immutable(unchanging) data structure',
#     }
# print("\nVariable: ")
# print(f"{glossary['variable']}.")
# print("\nLoop: ")
# print(f"{glossary['loop']}.")
# print("\nRange: ")
# print(f"{glossary['range']}.")
# print("\nSlice: ")
# print(f"{glossary['slice']}.")
# print("\nTuple: ")
# print(f"{glossary['tuple']}.")

# ### 6.4 Glossary 2

# # glossary = {
# #     'variable': 'data values that can change',
# #     'loop': 'sequence of instructions that is continually repeated',
# #     'range': 'set of possible values a variable can hold',
# #     'slice': 'a subset of data values in a dataset',
# #     'tuple': 'an immutable(unchanging) data structure',
# #     }

# glossary = {
#     'variable': 'data values that can change',
#     'loop': 'sequence of instructions that is continually repeated',
#     'range': 'set of possible values a variable can hold',
#     'slice': 'a subset of data values in a dataset',
#     'tuple': 'an immutable(unchanging) data structure',
#     'comments': 'notes in code that are not executed but provide information about the code',
#     'string': 'a series of characters (letters, numbers, punctuation, operators, etc',
#     'Dcipher87': 'a computer programmer and pythonista'
#     }

# for term, definition in glossary.items():
#     print(f"\n{term.title()}:")
#     print(definition)
# print("\n")

### 6.5 Rivers

# rivers = {
#     'nile': 'egypt',
#     'vaal': 'south africa',
#     'amazon': 'brazil',
#     'thames': 'england',
#     }

# for river, country in rivers.items():
#     if river == "thames":
#         print(f"The river {river.title()} runs through {country.title()}.")
#     else:
#         print(f"The {river.title()} river runs through {country.title()}.")
# print("The rivers included in the survery are:")
# for river in rivers.keys():
#     print(f"\t{river.title()}")
# print("\n")

# print("We will be considering rivers from the following countries:")
# for country in rivers.values():
#     print(f"\t{country.title()}")

# ### 6.6 Polling
# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# pollers = ['khaya', 'sarah', 'cairo', 'defjux', 'edward', 'lethu', 'enigma']

# for poller in pollers:
#     if poller in favourite_languages.keys():
#         print(f"Hi {poller.title()}! Thank you for taking the poll.")
#     else:
#         print(f"Hi {poller.title()}, please don't forget to take the poll by Friday.")