# ### Importing multiple Classes from a module
# from car import Car, ElectricCar

# my_beetle = Car("volkswagen", "beetle", 2018)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar("tesla", "roadster", 2020)
# print(my_tesla.get_descriptive_name())

# ### Importing an entire module

# import car

# my_beetle = car.Car("volkswagen", "beetle", 2018)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar("tesla", "roadster", 2020)
# print(my_tesla.get_descriptive_name())

### Importing all classes from a module

# from car import *

# my_beetle = Car("volkswagen", "beetle", 2018)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar("tesla", "roadster", 2020)
# print(my_tesla.get_descriptive_name())

# ### Importing a module into a module
# from car import Car 
# from electric_car import ElectricCar 

# my_beetle = Car("volkswagen", "beetle", 1999)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar("tesla", "roadster", 2020)
# print(my_tesla.get_descriptive_name())

### Using Aliases

from electric_car import ElectricCar as EC

my_tesla = EC("tesla", "model s", 2021)
print(my_tesla.get_descriptive_name())