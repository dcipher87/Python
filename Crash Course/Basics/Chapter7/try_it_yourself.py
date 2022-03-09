# ### 7.1 Rental Car

# requested_car = input("What car would you like to rent? ")
# print(f"Let me see if I can find a {requested_car.title()} for you. One moment please.")

# ### 7.2 Restaurant Seating

# dinner_guests = input("How many are in your dinner group? ")
# dinner_guests = int(dinner_guests)

# if dinner_guests > 8:
#     print("You'll have to wait for a table, feel free to visit the bar.")
# else:
#     print("Your waiter will escort you to your table.")

# ### 7.3 Multiples of Ten
# prompt = "Input a number and I will confirm if it is a multiple of 10. "
# prompt += "\nEnter a number: "

# number = input(prompt)
# number = int(number)

# if number % 10 == 0:
#     print(f"{number} is a multiple of 10.")
# else:
#     print(f"{number} is NOT a mulitple of 10") 

# ### 7.4 Pizza Toppings
# prompt = "Enter the pizza toppings you would like."
# prompt += "\nEnter 'quit' when you are finished. "

# #toppings = []
# topping = ""
# while topping != "quit":
#     topping = input(prompt)
#     if topping != "quit":
#         print(f"We'll add {topping.title()} to your order.")
#         #toppings.append(topping)
        
# print("Your have requested the following on your pizza: ")
# for topping in toppings:
#     print(f"\t{topping.title()}")
    
# ### 7.5 Movie Tickets

# prompt = "Enter your age to confirm ticket price."
# prompt += "\n(Enter 'quit' once all ages are entered). "

# while True:
#     age = input(prompt)

#     if age == "quit":
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             ticket = "Free"
#         elif age < 12:
#             ticket = "$10"
#         else: 
#             ticket = "$15"
#     print(f"Your ticket price is {ticket}.\n")

# ### 7.6 Three Exits
# prompt = "Enter the pizza toppings you would like."
# prompt += "\nEnter 'quit' when you are finished. "

# #toppings = []
# topping = ""
# while topping != "quit":
#     topping = input(prompt)

#     if topping != "quit":
#         print(f"We'll add {topping.title()} to your order.")
############################################################
# prompt = "Enter the pizza toppings you would like."
# prompt += "\nEnter 'quit' when you are finished. "

# #toppings = []
# active_order = True
# while active_order:
#     topping = input(prompt)

#     if topping == "quit":
#         active_order = False
#     else:        
#         print(f"We'll add {topping.title()} to your order.")
#         #toppings.append(topping)        
# ##############################################################
# prompt = "Enter the pizza toppings you would like."
# prompt += "\nEnter 'quit' when you are finished. "

# #toppings = []

# while True:
#     topping = input(prompt)

#     if topping == "quit":
#         break
#     else:        
#         print(f"We'll add {topping.title()} to your order.")
#         #toppings.append(topping)  
    
# ### 7.7 Infinity

# while True:
#     print("Inifity loop baby!")

# ### 7.8 Deli

# sandwich_orders = ["peanut butter and jam", "cheese and tomato", "egg and mayo", "ham and cheese", "tuna mayo"]
# finished_sandwiches = []

# sandwich_orders.reverse()

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"We have made your {current_sandwich.title()} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# #print(sandwich_orders)
# print("\nThe following sandwiches have been made: ")
# for sandwich in finished_sandwiches:
#     print(f"\t{sandwich.title()}")

# ### 7.9 No Pastrami
# sandwich_orders = ["pastrami","peanut butter and jam","pastrami", "cheese and tomato","pastrami", "egg and mayo","pastrami", "ham and cheese", "tuna mayo", "pastrami"]
# finished_sandwiches = []

# sandwich_orders.reverse()
# print("Apologies, pastrami shortage. No pastrami sandwiches will be made.")

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"We have made your {current_sandwich.title()} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# #print(sandwich_orders)
# print("\nThe following sandwiches have been made: ")
# for sandwich in finished_sandwiches:
#     print(f"\t{sandwich.title()}")

### 7.10 Dream Vacation

dream_vacations = {}

poll_active = True

while poll_active:
    name = input("What is your name? ")
    vacation = input("where would you like to vacation? ")
    
    dream_vacations[name] = vacation

    repeat = input("\nwould you like to retake the poll? (yes/no) ")
    repeat = repeat.lower()

    if repeat == "no":
        poll_active = False

print("\nResults:")
for name, vacation in dream_vacations.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")
