# ### 8.1 Message

# def display_message():
#     """Displays message about this chapter's topic"""
#     print("In chapter 8, I am learning about functions!")
#     print("Like the one I'm calling to print this!")

# display_message()

# ### 8.2 Favourite Book

# def favourite_book(title):
#     """Prints a sentence confirming favourite book"""
#     print(f"One of my favourite books is {title.title()}. I read it when I was young.")

# favourite_book("Alice in wonderland")
# favourite_book("Pet cemetary")
# favourite_book("Cellular")

# ### 8.3 T-Shirt
# def make_tshirt(size, printing):
#     """Displays shirt size and message to be printed on shirt"""
#     print(f"\nYou have ordered a {size} sized shirt, with the text '{printing}' on it.")

# make_tshirt("medium", "print('Hello World')")
# make_tshirt(printing="print('Hello python world!')", size="small")

# ### 8.4 Large Shirts
# def make_shirt(size="large", printing="I love Python!"):
#     """Displays shirt size and message to be printed on shirt"""
#     print(f"You have ordered a {size} sized shirt with the text {printing} on it.")

# make_shirt()
# make_shirt("medium")
# make_shirt("small", "World hello")

# ### 8.5 Cities

# def describe_city(city, country="south africa"):
#     """Displays city name and the country it's found in"""
#     print(f"\nI have been to {city.title()}, which is in {country.title()}.")

# describe_city("cape town")
# describe_city(city="durban")
# describe_city("maputo", "mozambique")
# describe_city(city="nairobi", country="kenya")

# ### 8.6 City Names
# def city_country(city, country):
#      """Returns a city, country pair neatly formatted"""
#      city_and_country = f"{city}, {country}"
#      return city_and_country.title()

# location = city_country("johannesburg", "south africa")
# print(location)
# location = city_country("lisbon", "portugal")
# print(location)
# location = city_country("paris", "france")
# print(location)

# ### 8.7 Album

# def make_album(artist, title, songs=None):
#      """Returns a dictionary with an albums artist and title"""
#      album = {'artist': artist, 'title': title}
#      if songs:
#           album['songs'] = songs
#      return album

# made_album = make_album('jimi hendrix', 'are you experienced')
# print(made_album)
# made_album = make_album('mf doom', 'food')
# print(made_album)
# made_album = make_album('aesop rock', 'the impossible kid')
# print(made_album)
# made_album = make_album('gorillaz', 'daemon days', 18)
# print(made_album)

# ### 8.8 User Albums
# def make_album(artist, title, songs=None):
#      """Returns a dictionary with an albums artist and title"""
#      album = {'artist': artist, 'title': title}
#      if songs:
#           album['songs'] = songs
#      return album

# while True:
#      print("\nEnter artist details for your music collection")
#      print("Enter 'q' any time to quit.")
#      artist = input("Enter album artist: ")
#      if artist == 'q':
#           break
#      title = input("Enter album title: ")
#      if artist == 'q':
#           break
#      songs = input("Number of songs: ")
#      if songs == 'q':
#           break

#      if songs:
#           my_album = make_album(artist, title, songs)
#           print(my_album)
#      else:
#           my_album = make_album(artist, title)
#           print(my_album)

# ### 8.9 Messages

# messages = ["please call me", "in a meeting", "driving, talk later", "please leave a message", "call back in 15"]

# def show_messages(message_list):
#     """Print messages from list"""
#     message_list.reverse()
#     print("These are you messages: ")
#     while message_list:
#         current_message = message_list.pop()
#         print(current_message)

# show_messages(messages)

# ### 8.10 Sending Messages
# messages = ["please call me", "in a meeting", "driving, talk later", "please leave a message", "call back in 15"]

# # def show_messages(message_list):
# #     """Print messages from list"""
# #     message_list.reverse()
# #     print("These are you messages: ")
# #     while message_list:
# #         current_message = message_list.pop()
# #         print(current_message)

# # show_messages(messages)
# sent_messages = []

# def send_message(unsent, sent):
#     """Prints messages and moves them to sent messages"""
#     unsent.reverse()
#     while unsent:
#         current_message = unsent.pop()
#         print(f"Sending message: {current_message}")
#         sent_messages.append(current_message)

# send_message(messages, sent_messages)

# print(messages)
# print(sent_messages)

# ### 8.11 Archived Messages
# messages = ["please call me", "in a meeting", "driving, talk later", "please leave a message", "call back in 15"]
# sent_messages = []

# def send_message(unsent, sent):
#     """Prints messages and moves them to sent messages"""
#     unsent.reverse()
#     while unsent:
#         current_message = unsent.pop()
#         print(f"Sending message: {current_message}")
#         sent_messages.append(current_message)

# send_message(messages[:], sent_messages)

# print(messages)
# print(sent_messages)

# ### 8.12 Sandwiches
# def make_sandwich(*fillings):
#     """Summarise the fillings requested for a sandwich"""
#     print("\nYour sandwich will contain the following: ")
#     for fill in fillings:
#         print(f"- {fill.title()}")

# make_sandwich("peanut butter and jam")
# make_sandwich("tuna", "mayo")
# make_sandwich("bacon", "lettuce", "tomato")

# ### 8.13 User Profile

# def build_profile(first_name, last_name, **user_info):
#     """Display all info we have for a user"""
#     user_info['first_name'] = first_name
#     user_info['last_name'] = last_name
#     return user_info

# user_profile = build_profile("khaya", "ubisi", location="johannesburg", occupation="software developer", hobby="unicycling", food="pizza")

# print(user_profile)

# print("\nUser info:" )
# for key, value in user_profile.items():
#     print(f"{key.title()}: {value.title()}")

# ### 8.14 Cars
# def make_car(make, model, **extras):
#     """Prints the details of requested car"""
#     extras['make'] = make
#     extras['model'] = model
#     return extras

# def display_car(extras):
#     """Print confirmation of requested car details"""
#     print("\nYou have requested the following car: ")
#     for key, value in extras.items():
#         print(f"\t- {key.title()}: {value.title()}")


# requested_car = make_car("honda", "civic", color="white", towbar="True", sunroof="True")

# display_car(requested_car)

# requested_car = make_car("subaru", "outback", color="blue", sportspackage="True")

# display_car(requested_car)

# ### 8.15 Printing Models

# from printing_functions import print_models as pm, confirm_printed as cp 

# to_print = ["bluetooth speaker", "headphones", "rubber duck", "photo frame", "vase"]
# printed = []

# pm(to_print, printed)
# cp(printed)

### 8.16 Imports
# import build_profile

# my_profile =  build_profile.build_profile("khaya", "ubisi", age=34, occupation="junior software engineer", location="johannesbug")

# #print(my_profile)

# print("User details: ")
# for key, value in my_profile.items():
#     if key == 'age':
#         print(f"\t-{key.title()}: {value}")
#     else:
#         print(f"\t-{key.title()}: {value.title()}")

# from build_profile import build_profile as bp

# my_profile =  bp("khaya", "ubisi", age=34, occupation="junior software engineer", location="johannesbug")

# #print(my_profile)

# print("User details: ")
# for key, value in my_profile.items():
#     if key == 'age':
#         print(f"\t-{key.title()}: {value}")
#     else:
#         print(f"\t-{key.title()}: {value.title()}")

# import build_profile as bp

# my_profile =  bp.build_profile("khaya", "ubisi", age=34, occupation="junior software engineer", location="johannesbug")

# #print(my_profile)

# print("User details: ")
# for key, value in my_profile.items():
#     if key == 'age':
#         print(f"\t-{key.title()}: {value}")
#     else:
#         print(f"\t-{key.title()}: {value.title()}")

from build_profile import *

my_profile =  build_profile("khaya", "ubisi", age=34, occupation="junior software engineer", location="johannesbug")

#print(my_profile)

print("User details: ")
for key, value in my_profile.items():
    if key == 'age':
        print(f"\t-{key.title()}: {value}")
    else:
        print(f"\t-{key.title()}: {value.title()}")