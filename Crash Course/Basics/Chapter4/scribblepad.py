# ### 4.1 Pizzas
# pizzas = ["something meaty", "chicken and mushroom", "bacon and fet", "hawaii", "triple decker" ]

# for pizza in pizzas:
#     print(f"I love {pizza.title()}! It's my favourite.")

# print("I just love pizza man!")

# ### 4.1 Animals
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

 ### 4.10 Slices
cars = ["vw", "bmw", "suzuki", "jeep", "lotus", "porsche", "ferrari"]
print("The first three items on this list are: ")
for car in cars[:3]:
    print(car.title())
