players = ["charles", "martina", "michael", "florence", "eli"]

# print(players[0:3])
# print(players[:3]) # same as above - omit first index python starts splice at begining of list

# print(players[1:4])

# print(players[2:5])
# print(players[2:]) # same as above - omit last index python ends slice at the end of the list

# print(players[-3:]) # negative numbers return slice values a certain index from the end of the list
# print(players[-2:])

# print(players[0:5:2]) # third splice argument confirms how many list items to skip, eg: every even or odd indexed list item.

for player in players[-3:]: # looping through a slice
    print(player.title())
