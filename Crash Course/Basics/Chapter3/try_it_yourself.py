# All the try it yourself exercise from chapter 3

# ### 3.1 Names
# names = ["khaya", "khigha", "cairo", "funcrusher", "nettcaster"]

# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[-2].title())
# print(names[-1].title())

# ### 3.2 Greetings
# names = ["khaya", "khigha", "cairo", "funcrusher", "nettcaster"]

# message = f"Hi there {names[0]}! I hear you're learning Python. All the best!"
# print(message)
# message = f"Hi there {names[1]}! I hear you're learning Python. All the best!"
# print(message)
# message = f"Hi there {names[2]}! I hear you're learning Python. All the best!"
# print(message)
# message = f"Hi there {names[3]}! I hear you're learning Python. All the best!"
# print(message)
# message = f"Hi there {names[4]}! I hear you're learning Python. All the best!"
# print(message)

# for name in names:
#     print(f"Hi there {name.title()}! I hear you're learning Python. All the best!")

# ### 3.3 Your own list
# transportation = ["motorcycle", "car", "bicycle", "train", "airplane"]

# message = f"I would like to own a Honda {transportation[0]}."
# print(message)

# message = f"I drive a VW Polo GT {transportation[1]}."


# print(message)

# message = f"When I was young my {transportation[2]} was stolen"
# print(message)

# message = f"When I started work I took the {transportation[3]} a lot!"
# print(message)

# message = f"I fly in an {transportation[4]} to Cape Town to visit my cousin."
# print(message)

# ### 3.4 Guest list
# guests = ["aesop rock", "jimi hendrix", "beyonce", "mf doom", "thomas sankara"]

# message = f"Hi {guests[0].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[1].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[2].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[3].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[4].title()}, here is a dinner invite, come through!"
# print(message)

# ### 3.5 Changing guest list
# guests = ["aesop rock", "jimi hendrix", "beyonce", "mf doom", "thomas sankara"]

# new_guest = "rihanna"
# guests.append(new_guest)
# cancelled_guest = "beyonce"
# guests.remove(cancelled_guest)

# message = f"Hi {guests[0].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[1].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[2].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[3].title()}, here is a dinner invite, come through!"
# print(message)

# message = f"Hi {guests[4].title()}, here is a dinner invite, come through!"
# print(message)

# print(f"{cancelled_guest.title()} will be unable to attend our dinner, we have extended the invite to {new_guest.title()} instead.")


# guests = ["aesop rock", "jimi hendrix", "beyonce", "mf doom", "thomas sankara"]
# guests[2] = "rihanna"
# # print(guests)

# guests.insert(0, "nas")
# guests.insert(3, "nthabi")
# guests.append("ronaldo")

# print(guests)

# message = f"Good day {guests[0].title()}. Kindly accept my dinner invitation attached."
# print(message)

# message = f"Good day {guests[1].title()}. Kindly accept my dinner invitation attached."
# print(message)

# message = f"Good day {guests[2].title()}. Kindly accept my dinner invitation attached."
# print(message)

# message = f"Good day {guests[3].title()}. Kindly accept my dinner invitation attached."
# print(message)

# message = f"Good day {guests[4].title()}. Kindly accept my dinner invitation attached."
# print(message)

# message = f"Good day {guests[5].title()}. Kindly accept my dinner invitation attached."
# print(message)

# message = f"Good day {guests[6].title()}. Kindly accept my dinner invitation attached."
# print(message)


# message = f"Good day {guests[7].title()}. Kindly accept my dinner invitation attached."
# print(message)

# for guest in guests:
#     print(f"Good day {guest.title()}. Kindly accept my dinner invitation attached.")

# print("\nHi all, we have found a bigger table for our reservation, more guests will be joining us. See you soon.")

# ### 3.7 Shrinking guest list
# guests = ["aesop rock", "jimi hendrix", "beyonce", "mf doom", "thomas sankara"]
# guests[2] = "rihanna"
# # print(guests)

# guests.insert(0, "nas")
# guests.insert(3, "nthabi")
# guests.append("ronaldo")

# print("Hi all, unfortunately my new table will not arrive in time for the dinner party. I can only invite 2 guests. Please check your emails for further communication.\n")
# print(guests)

# cancelled_guest = guests.pop()
# print(f"Hi {cancelled_guest.title()}, please accept my sincerest apologies, I can no longer host you at my dinner party.")
# cancelled_guest = guests.pop()
# print(f"Hi {cancelled_guest.title()}, please accept my sincerest apologies, I can no longer host you at my dinner party.")
# cancelled_guest = guests.pop()
# print(f"Hi {cancelled_guest.title()}, please accept my sincerest apologies, I can no longer host you at my dinner party.")
# cancelled_guest = guests.pop()
# print(f"Hi {cancelled_guest.title()}, please accept my sincerest apologies, I can no longer host you at my dinner party.")
# cancelled_guest = guests.pop()
# print(f"Hi {cancelled_guest.title()}, please accept my sincerest apologies, I can no longer host you at my dinner party.")
# cancelled_guest = guests.pop()
# print(f"Hi {cancelled_guest.title()}, please accept my sincerest apologies, I can no longer host you at my dinner party.")

# print(f"Hi {guests[0].title()}, I would still like you to attend my dinner party.")
# print(f"Hi {guests[1].title()}, I would still like you to attend my dinner party.")

# del guests[0]
# del guests[0]
# print(guests)

#############
# guests = ["aesop rock", "jimi hendrix", "beyonce", "mf doom", "thomas sankara"]
# guests[2] = "rihanna"
# # print(guests)

# guests.insert(0, "nas")
# guests.insert(3, "nthabi")
# guests.append("ronaldo")

# print("I can only invite 2 of yall")
# while len(guests) > 2:
#     cancelled_guest = guests.pop()
#     print(f"Hi {cancelled_guest.title()}, sorry you're uninvited now.")
# print(guests)    

# for guest in guests:
#     print(f"Hi {guest.title()}, we're still on for dinner.")

# while len(guests) > 0:
#     del guests[0]    
    
# print(guests)    

# ### 3.8 Seeing the world
# places = ["lisbon", "cairo", "manchester", "new york", "milan", "amsterdam"]
# print(places)

# print(sorted(places))
# print(places)

# print(sorted(places, reverse=True))
# print(places)

# places.reverse()
# print(places)
# places.reverse()
# print(places)

# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)

### Dinner guests
# guests = ["aesop rock", "jimi hendrix", "beyonce", "mf doom", "thomas sankara"]
# print(f"There will be {len(guests)} guests at the dinner party")

# ### 3.10 Every function
# soccer_teams = ["manchester united", "real madrid", "inter milan", "ajax amsterdam", "lyon"]

# print(soccer_teams)
# soccer_teams.append("benfica")
# print(soccer_teams)
# soccer_teams.insert(0, "young boys")
# print(soccer_teams)

# relegated = soccer_teams.pop()
# print(f"{relegated.title()} was relegated.")
# print(soccer_teams)

# del soccer_teams[0]
# print(soccer_teams)

# unfan = soccer_teams.pop(4)
# print(f"I don't really watch {unfan.title()} much.")
# print(soccer_teams)

# soccer_teams.append("chelsea")
# soccer_teams.append("liverpool")
# print(soccer_teams)

# soccer_teams.remove("chelsea")
# print(soccer_teams)
# soccer_teams.remove("liverpool")
# print(soccer_teams)

# soccer_teams.sort()
# print(soccer_teams)

# soccer_teams.sort(reverse=True)
# print(soccer_teams)

# print(sorted(soccer_teams))
# print(sorted(soccer_teams, reverse=True))

# soccer_teams.reverse()
# print(soccer_teams)
# print(len(soccer_teams))