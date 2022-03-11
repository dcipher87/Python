# def make_pizza(*toppings):
#     """Prints the list of toppings that have been requested"""
#     print(toppings)

# make_pizza("pepperoni")
# make_pizza("mushrooms", "green pepper", "extra cheese")
def make_pizza(*toppings):
    """Summarise the pizza with requested toppings"""
    print("\nYou've ordered a pizza with the following topping(s):")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza("pepperoni")
make_pizza("mushrooms", "extra cheese", "green peppers")

