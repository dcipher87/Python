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

# ### 6.7 People

# # from 6.1 
# kubisi = {
#     'first_name': 'khaya',
#     'last_name': 'ubisi', 
#     'age': 34,
#     'city': 'johannesburg',
#     }
# klethu = {
#     'first_name': 'khigha',
#     'last_name': 'lethu',
#     'age': 30,
#     'city': 'boksburg',
#     }
# cdilbert = {
#     'first_name': 'cairo',
#     'last_name': 'dilbert',
#     'age': 25,
#     'city': 'springs',
#     }
# dcipher = {
#     'first_name': 'defjux',
#     'last_name': 'cipher',
#     'age': 30,
#     'city': 'midrand',
#     }
# # Tile with full name, age and city
# # Sentence with full name, age and city

# people = [kubisi, klethu, cdilbert, dcipher]
# # print("\nWe have the following active users: ")
# # for person in people:
# #     full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
# #     age = person['age']
# #     city = person['city'].title()
# #     print(f"\n\tFull name: {full_name}")
# #     print(f"\tAge: {age}")
# #     print(f"\tCity: {city}")    

# print("We have the following users: ")
# for person in people:
#     full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     age = person['age']
#     city = f"{person['city'].title()}"
#     print(f"{full_name} is a {age} year old from {city}.")

# ### 6.8 Pets

# earthwormjim = {
#     'name': 'earth worm jim',
#     'species': 'house snake',
#     'order': 'first',
#     'morph': 'normal',
#     }
# adamantium = {
#     'name': 'adamantium',
#     'species': 'red-tail boa',
#     'order': 'second',
#     'morph': 'albino',
#     }
# eve = {
#     'name': 'eve',
#     'species': 'dumerils boa',
#     'order': 'third',
#     'morph': 'normal',
#     }
# lilith = {
#     'name': 'lilith',
#     'species': 'amazon tree boa',
#     'order': 'fourth',
#     'morph': 'normal',
#     }
# apple = {
#     'name': 'apple',
#     'species': 'rosy boa',
#     'order': 'fifth',
#     'morph': 'normal',
#     }
# my_pets = [earthwormjim, adamantium, eve, lilith, apple]

# print("These are all my snakes: \n")
# for pet in my_pets:
#     # variables 
#     name = pet['name'].title()
#     species = pet['species'].title()
#     order = pet['order']
#     morph = pet['morph']

#     # print(f"{name} was my {order} snake, she's a {morph} {species}." )
#     print(f"Name: {name}")
#     print(f"Species: {species}")
#     print(f"Morph: {morph}\n")

# ### 6.9 Favourite Places

# favourite_places = {
#     'khaya': {
#         'city': 'amsterdam',
#         'country': 'portugal',
#         'town': 'springs',
#         },
#     'khigha': {
#         'city': 'new york',
#         'country': 'kenya',
#         'town': 'boksburg',
#         },
#     'cairo': {
#         'city': 'london',
#         'country': 'egypt',
#         'town': 'brooklyn',
#         },
#     }
# for name, places in favourite_places.items():
#     print(f"{name.title()}'s favourite places are: ")
#     for location, place in places.items():
#         print(f"Favourite {location.title()} is {place.title()}.")
#     print("\n")
        
# ### 6.10 Favourite Numbers

# favourite_numbers = {
#     'khaya': [13, 23, 64],
#     'khigha': [7, 95, 136, 4363],
#     'defjux': [34, 4, 22, 6, 356, 43],
#     'strife': [144, 23, 65, 44],
#     'enigma': [9, 45, 5],
#     }

# for name, numbers in favourite_numbers.items():
#     print(f"\n{name.title()}'s favourite numbers are: ")
#     for number in numbers:
#         print(number)

# ### 6.11 Cities 
# #sandton, lisbon, manchester, new york, tokyo, sydney
# cities = {
#     'sandton': {
#         'country': 'south africa',
#         'population': 222415,
#         'fact': 'Sandton is home to Sandton Convention Centre, one of the largest convention centres on the continent.',
#         },
#     'lisbon': {
#         'country': 'portugal',
#         'population': 504718,
#         'fact': 'Lisbon is one of Europe\'s oldest cities and oldest capitals, inhabited since around 205BC.',
#         },
#     'manchester': {
#         'country': 'united kingdom',
#         'population': 553230,
#         'fact': 'Manchester is where the atom was split for the first time',
#         },
# }
# for city, info in cities.items():
#     print(city.title())
#     for topic, details in info.items():
#         if topic == 'country':
#             print(f"{topic.title()}: {details.title()}")
#         else:   
#             print(f"{topic.title()}: {details}")
#     print("\n")        

### 6.12 Extensions

