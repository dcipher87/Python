# ### 4.1 Pizzas
# pizzas = ["something meaty", "chicken and mushroom", "bacon and fet", "hawaii", "triple decker" ]

# for pizza in pizzas:
#     print(f"I love {pizza.title()}! It's my favourite.")

# print("I just love pizza man!")

# ### 4.2 Animals
# animals = ["amazon tree boa", "boa constrictor", "rainbow boa", "rubber boa", "yellow anaconda"]

# for snake in animals:
#     print(f"You know, a {snake.title()} would make such a good pet")
# print("Any of these reptiles would make awsome pets!")

# ### 4.3 Counting to twenty
# for i in range(21):
#     print(i)

# ### 4.4 One Million
# million = list(range(1000000))
# for number in million:
#     print(number)

# ### 4.5 Summing a million
# numbers = list(range(1000001))

# # for number in numbers:
# #     print(number)

# print(sum(numbers)) 

# ### 4.6 Odd number
# odd_numbers = list(range(1, 21, 2))
# for odd in odd_numbers:
#     print(odd)

# ### 4.7 Threes
# threes = list(range(3, 31, 3))
# print(threes)

# ### 4.8 Cubes
# numbers = list(range(11))
# cubes = []

# for number in numbers:
#     cube = number ** 3
#     cubes.append(cube)
#     print(cube)
# print(cubes)

# ### 4.9 Cube comprehension
# cubes = [cube **3 for cube in range(1, 11)]
# print(cubes)

#  ### 4.10 Slices
# cars = ["vw", "bmw", "suzuki", "jeep", "lotus", "porsche", "ferrari"]
# print("The first three items on this list are: ")
# for car in cars[:3]:
#     print(car.title())

# cars = ["vw", "bmw", "suzuki", "jeep", "lotus", "porsche", "ferrari"]
# print("The middle three items on this list are: ")
# for car in cars[2:5]:
#     print(car.title())

# cars = ["vw", "bmw", "suzuki", "jeep", "lotus", "porsche", "ferrari"]
# print("The last three items on this list are: ")
# for car in cars[-3:]:
#     print(car.title())

# ### 4.11 My Pizzas, Your Pizzas

# pizzas = ["something meaty", "chicken and mushroom", "bacon and fet", "hawaii", "triple decker" ]
# friends_pizza = pizzas[:]
# print(pizzas)
# print(friends_pizza)

# pizzas.append("club")
# friends_pizza.append("mexican chilli")
# print(pizzas)
# print(friends_pizza)

# print("\nMy favourite pizzas are:")
# for pizza in pizzas:
#     print(f"\t{pizza.title()}")

# print("\nMy friends' favourite pizzas are:")
# for pizza in friends_pizza:
#     print(f"\t{pizza.title()}")

# ### 4.12 More loops
# my_foods = ["pizza", "falafel", "carrot cake"]
# friends_food = my_foods[:]

# friends_food.append("ice cream")
# print(my_foods)
# print(friends_food)

# print("My foods are: ")
# for food in my_foods:
#     print(food.title())

# print("My friends' foods are: ")
# for food in friends_food:
#     print(food.title())

### 4.13 Buffet
# dimensions = (200, 50)
# print(dimensions)
# dimensions[0] = 250

# foods = ("pap and wors", "rice and curry", "beef stew", "bunny chow", "kota", "pie", "fish and chips")
# # print("The restaurant serves the following foods: ")
# # for food in foods:
# #     print(food.title())

# # foods[2] = "hot dogs"    

# foods = ("pap and wors", "rice and curry", "beef stew", "bunny chow", "kota", "pie", "fish and chips")

# print(foods)

# foods = ("pap and wors", "rice and curry", "salad", "sandwich", "kota", "pie", "fish and chips")
# print(foods)

# print("The restaurant now serves these meals: ")
# for food in foods:
#     print(food.title())
