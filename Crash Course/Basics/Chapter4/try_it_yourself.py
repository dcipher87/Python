### 4.1 Pizzas

# pizzas = ["chicken and mushroom", "meat lovers", "triple decker", "bacon and feta"]

# for pizza in pizzas:
#     # print(pizza.title())
#     print(f"I love {pizza.title()} pizza. It's my favourite!")
# print("\nI just really love pizza! Like a ninja turtle!")

# ### 4.2 Animals

# animals = ["dog", "cat", "snake", "lizard", "hamster"]

# for animal in animals:
#     print(f"A {animal} would make a great pet.")
# print("All these animals would make great pets.")

# ### 4.3 Counting to Twenty
# for value in range(1, 21):
#     print(value)

# ### 4.4 One Million
# numbers = list(range(1, 1000001))
# # for number in numbers:
# #     print(number)

### 4.5 Summing a Million
# numbers = list(range(1, 1000001))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# ### 4.6 Odd Numbers
# numbers = list(range(1, 21, 2))
# for num in numbers:
#     print(num)

# for num in list(range(1, 21, 2)):
#     print(num)

# ### 4.7 Threes
# threes = list(range(3, 31, 3))
# for num in threes:
#     print(num)

# for num in list(range(3, 31, 3)):
#     print(num)

# ### 4.8 Cubes and 4.9 Cube Comprehension
# cubes = [num**3 for num in range(1, 11)]
# for cube in cubes:
#     print(cube)


# ### 4.10 Slices
# pizzas = ["chicken and mushroom", "meat lovers", "triple decker", "bacon and feta", "double stack"]

# print("The first three items on the list are:")
# for pizza in pizzas[:3]:
#     print(pizza.title())

# print("The items from the middle of the list are:")
# for pizza in pizzas[1:4]:
#     print(pizza.title())


# print("The last threee items in the list are:")
# for pizza in pizzas[-3:]:
#     print(pizza.title())

# ### 4.11 My Pizzas, Your Pizzas
# pizzas = ["chicken and mushroom", "meat lovers", "triple decker", "bacon and feta"]
# friend_pizzas = pizzas[:]

# pizzas.append("hawaiian")
# friend_pizzas.append("club")

# print("My favourite pizzas are:")
# for pizza in pizzas:
#     print(pizza.title())

# print("\nMy friend's favourite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza.title())

# ### 4.12 More Loops
# my_foods = ["pizza", "falafel", "carrot cake"]
# friend_food = my_foods[:]

# print(my_foods)
# print(friend_food)

# my_foods.append("cheese burger")
# friend_food.append("ice-cream")

# print("My favourite foods are:")
# for food in my_foods:
#     print(food.title())

# print("\nMy friend's favourite foods are:")
# for food in friend_food:
#     print(food.title())

### 4.13 Buffet
menu_foods = ("beef stew", "butter chicken", "fish and chips", "lamb curry", "pizza", "hotdog", "burger")

print(menu_foods)
print("\n")
for food in menu_foods:
    print(food.title())
print("\n")

# menu_foods[3] = "pepper steak pie"
# print(menu_foods)

menu_foods = ("veggie stew", "butter chicken", "russian and chips", "lamb curry", "pizza", "sausage roll", "burger")
for food in menu_foods:
    print(food.title())