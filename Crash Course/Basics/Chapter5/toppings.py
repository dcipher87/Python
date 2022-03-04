# Check for inequality
# requested_topping = "mushrooms"

# if requested_topping != "anchovies":
#     print("Hold the anchovies")

# requested_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms.")
# if "pepperoni" in requested_toppings:
#     print("Adding pepperoni.")
# if "extra cheese" in requested_toppings:
#     print("Adding extra chesse.")
# print("\nFinished making your pizza!")

# Type BMW in uppercase and all other car brands in titlecase
# cars = ["bmw", "audi", "toyota", "subaru"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# Check if item contained in list before proceeding loop
# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# for topping in requested_toppings:
#     if topping == "green peppers":
#         print(f"Sorry, we are out of {topping}.")
#     else:
#         print(f"Adding {topping.title()} to your pizza.")
# print("\nFinished making your pizza!")

# # Check if list is emptyp before we loop through it
# requested_toppings = []

# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping.title()} to your pizza.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping.title()} to your pizza.")
    else:
        print(f"Sorry we do not have {topping.title()} available as a topping.")
print("\nFinished making your pizza!")

# # Show added toppings first and unavailable toppings last
# for topping in requested_toppings:
#     if topping in available_toppings:
#         print(f"Adding {topping.title()} to your pizza.")
# for topping in requested_toppings:
#     if topping not in available_toppings:
#         print(f"{topping.title()} is not available as a toppping.")
# print("\nFinished making your pizza.")