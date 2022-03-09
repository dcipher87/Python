# alien_0 = {"color": "green", "points": 5}

# print(alien_0["color"])
# print(alien_0["points"])
# print(alien_0)

# new_points = alien_0["points"]
# print(f"You have just earned {new_points} points!")

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25

# print(alien_0)

# ### Starting with an empty dictionary, then populating it

# alien_0 = {}
# print(alien_0)

# alien_0["color"] = "green"
# alien_0["points"] = 5

# print(alien_0)

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25

# print(alien_0)

# ### Modifying values in a Dictionary

# alien_0 = {"color": "green"}
# # print(alien_0)
# print(f"The alien is {alien_0['color']}.")

# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
# print(f"Original position: {alien_0['x_position']}")

# # move the alien to the right
# # determine how far to move th alien based on its current speed

# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     #must be a fast alien
#     x_increment = 3

# # The position is the old position plus the increment
# alien_0["x_position"] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# alien_0["speed"] = "fast"

# # Removing Key-Value Pairs
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

### Nesting

# List of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# print(aliens[0]['color'])

# print("The colors we have chosen for the aliens are:")
# for alien in aliens:
#   print(alien['color'].title())

# print("The aliens will have the following points values:")
# for alien in aliens:
#     print(alien['points'])

# print("The aliens in our games will have the following characteristics:")
# for alien in aliens:
#     print(f"The {alien['color'].title()} alien will be worth {alien['points']} points.")

# Make 30 aliens

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # print(aliens)    

# # Show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)

# # Show number of aliens created
# print(f"Total number of aliens: {len(aliens)}.")

# aliens = []

# for number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # print(len(aliens))
# # print(aliens[:5])

# for alien in aliens[:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'

# print(len(aliens))

# for alien in aliens[:10]:
#     print(alien)

# aliens = []

# for number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # print(len(aliens))
# # print(aliens[:5])

# for alien in aliens[:5]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'

# for alien in aliens[:10]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['points'] = 15
#         alien['speed'] = 'fast'


# print(len(aliens))

# for alien in aliens[:15]:
#     print(alien)