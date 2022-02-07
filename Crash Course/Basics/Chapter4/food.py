# my_foods = ["pizza", "falafel", "carrot cake"]
# friends_food = my_foods[:]

# print("My favoutie foods are:")
# print(my_foods)

# print("\nMy friend's favourite foods are:")
# print(friends_food)

# my_foods.append("cheese burger")
# friends_food.append("fried chicken")
# print("\n")

# print("My favoutie foods are:")
# print(my_foods)

# print("\nMy friend's favourite foods are:")
# print(friends_food)

my_foods = ["pizza", "falafel", "carrot cake"]
friend_food = my_foods # this doesn't copy the list, it creates an additonal variable pointing to the same list.

print(my_foods)
print(friend_food)

my_foods.append("cheese burger")
friend_food.append("fried chicken")

print(my_foods)
print(friend_food)

