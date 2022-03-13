# import pizza #imports whole module, all functions within module

# pizza.make_pizza(15, "pepperoni")
# pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# from pizza import make_pizza #imports specified functions from module (from module_name import function_1, function_2, etc)

# make_pizza(15, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# # Using an Alias for a function
# from pizza import make_pizza as mp #gives make_pizza a nickname of mp which can be used to call make_pizza  

# mp(15, "pepperoni")
# mp(12, "mushrooms", "green peppers", "extra cheese")

# # Using an Alias for a Module
# import pizza as p

# p.make_pizza(15, "pepperoni")
# p.make_pizza(12, "mushrooms", "green pepper", "extra cheese")

# Importing all functions in a Module
from pizza import * # allows functions to be called without dot notation

make_pizza(15, "pepperoni")
make_pizza(12, "extra cheese", "mushrooms", "green peppers")



