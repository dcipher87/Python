# def make_pizza(*toppings):
#     """Prints the list of toppings that have been requested"""
#     print(toppings)

# make_pizza("pepperoni")
# make_pizza("mushrooms", "green pepper", "extra cheese")
# def make_pizza(*toppings):
#     """Summarise the pizza with requested toppings"""
#     print("\nYou've ordered a pizza with the following topping(s):")
#     for topping in toppings:
#         print(f"- {topping.title()}")


# make_pizza("pepperoni")
# make_pizza("mushrooms", "extra cheese", "green peppers")

# Mixing positional and arbitrary arguments

# def make_pizza(size, *toppings):
#     """Summarise pizza size and toppings to be made"""
#     print(f"\nYou have requested a {size} inch pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping.title()}")

# make_pizza(15, "pepperoni")
# make_pizza(12, "mushrooms", "extra cheese", "green peppers")

####################Importing Modules Exercise###################

def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make"""
    print(f"\nMake a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")
        

