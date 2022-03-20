### String concatenation (how to put strings together)

# We want to create a string that says "Subscribe to _____"
youtuber = "Khaya Ubisi" # some string variable - youtuber's name

# a few ways to do this 

# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj.lower()}! It make makes me so exited all the time. I love to {verb1.lower()}. Stay hydrated and {verb2.lower()} like you are {famous_person.title()}!"

print(madlib)