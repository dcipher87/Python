# ### 9.1 Restaurant

# class Restaurant:
#     """A simple restaurant class/model"""

#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type.title()

#     def describe_restaurant(self):
#         """Describe the restaurant"""
#         print(f"{self.name} is a {self.cuisine_type} family restaurant.")

#     def open_restaurant(self):
#         """Confirms that the restaurant is open"""
#         print(f"{self.name} is open untill 20:00.")

# my_restaurant = Restaurant("Nandos", "Portuguese")

# print(f"My favorite place to eat is {restaurant.name}.")
# print(f"They serve {restaurant.cuisine_type} food, which is my favourite.")

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# ### 9.2 Restaurant

# my_restaurant = Restaurant("Mochachos", "mexican")
# my_restaurant.describe_restaurant()

# my_restaurant = Restaurant("Yankees", "american")
# my_restaurant.describe_restaurant()

# my_restaurant = Restaurant("KFC", "american")
# my_restaurant.describe_restaurant()

# ### 9.3 Users

# class User:
#     """Class that contains user data"""
#     def __init__(self, first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.city = city.title()
#         self.occupation = occupation.title()
#         self.phone_number = phone_number
#         self.email_addess = email_address
#         self.hobby = hobby
#         self.music_genre = music_genre
#         self.sport = sport
#         self.favourite_food = favourite_food

#     def describe_user(self):
#         print("\nUser details ")
#         print(f"Full name: {self.first_name} {self.last_name}")
#         print("User contact details ")
#         print(f"Cell: {self.phone_number} \tEmail: {self.email_addess}")
#         print("General information ")
#         print(f"{self.first_name} is a(n) {self.occupation} from {self.city}. He enjoys {self.hobby}, listening to {self.music_genre} music, watching {self.sport} and eating {self.favourite_food}.")

#     def greet_user(self):
#         print(f"Hello there {self.first_name}, how's the coding going?")

# my_user = User("khaya", "ubisi", "johannesburg", "web developer", "0731151085", "kubisi@gmil.com", "chess", "rock", "footbal", "pizza")

# my_user.describe_user()
# my_user.greet_user()

# my_user = User("lethu", "ubisi", "springs", "software tester", "0359395497", "lethu.bc@yayay.cc", "unicyling", "rap", "cricket", "braai meat")

# my_user.describe_user()
# my_user.greet_user()

# my_user = User("Khigha", "Machina", "lisbon", "web developer", "97430443999", "khigha@k.com", "gaming", "punk rock", "hockey", "hamburgers")

# my_user.describe_user()
# my_user.greet_user()

### 9.4 Number Served

# class Restaurant:
#     """A simple restaurant class/model"""

#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type.title()
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Describe the restaurant"""
#         print(f"{self.name} is a {self.cuisine_type} family restaurant.")

#     def open_restaurant(self):
#         """Confirms that the restaurant is open"""
#         print(f"{self.name} is open untill 20:00.")

#     def set_number_served(self, served_customers):
#         self.number_served = served_customers
    
#     def increment_number_served(self, customers_today):
#         self.number_served += customers_today

# new_restaurant = Restaurant("Steers", "beef")
#print(new_restaurant.number_served)

# # Directly modify attribute value
# new_restaurant.number_served = 45
# print(new_restaurant.number_served)

# Method modifies attribute value
# print(new_restaurant.number_served)
# new_restaurant.set_number_served(145)
# print(new_restaurant.number_served)

# new_restaurant.set_number_served(248)
# print(new_restaurant.number_served)

# # Method increments attributes
# print(new_restaurant.number_served)
# new_restaurant.increment_number_served(36)
# print(new_restaurant.number_served)
# new_restaurant.increment_number_served(335)
# print(new_restaurant.number_served)

### 9.5 Login Attempts

# class User:
#     """Class that contains user data"""
#     def __init__(self, first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.city = city.title()
#         self.occupation = occupation.title()
#         self.phone_number = phone_number
#         self.email_addess = email_address
#         self.hobby = hobby
#         self.music_genre = music_genre
#         self.sport = sport
#         self.favourite_food = favourite_food
#         self.login_attempts = 0

#     def describe_user(self):
#         """Displays all user information."""
#         print("\nUser details ")
#         print(f"Full name: {self.first_name} {self.last_name}")
#         print("User contact details ")
#         print(f"Cell: {self.phone_number} \tEmail: {self.email_addess}")
#         print("General information ")
#         print(f"{self.first_name} is a(n) {self.occupation} from {self.city}. He enjoys {self.hobby}, listening to {self.music_genre} music, watching {self.sport} and eating {self.favourite_food}.")

#     def greet_user(self):
#         """Displays a simple user greeting."""
#         print(f"Hello there {self.first_name}, how's the coding going?")

#     def increment_login(self):
#         """Increments login attempts."""
#         self.login_attempts += 1

#     def reset_logins(self):
#         self.login_attempts = 0

# new_user = User("khigha", "ubisi", "johannesburg", "front-end developer", "0723492354", "khi.ub@gmail.co", "chess", "hip-hop", "football", "pasta")

# print(new_user.login_attempts)

# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()

# print(new_user.login_attempts)

# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()
# new_user.increment_login()

# print(new_user.login_attempts)

# new_user.reset_logins()

# print(new_user.login_attempts)

# ### 9.6 Ice Cream Stand

# class Restaurant:
#     """A simple restaurant class/model"""

#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type.title()
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Describe the restaurant"""
#         print(f"{self.name} is a {self.cuisine_type} family restaurant.")

#     def open_restaurant(self):
#         """Confirms that the restaurant is open"""
#         print(f"{self.name} is open untill 20:00.")

#     def set_number_served(self, served_customers):
#         self.number_served = served_customers
    
#     def increment_number_served(self, customers_today):
#         self.number_served += customers_today

# class IceCreamStand(Restaurant):
#     """Represents aspects of a restaurant specific to an ice-cream stand."""
#     def __init__(self, name, cuisine_type):
#         """Initiates attributes about the parent class."""
#         super().__init__(name, cuisine_type)
#         self.flavours = ["vanilla", "chocolate", "caramel", "mint", "strawberry"]

#     def display_flavours(self):
#         """Displays all the flavours available."""
#         print("\nThe following flavours are available: ")
#         for flavour in self.flavours:
#             print(f"\t-{flavour.title()}")
    
# ice_cream_truck = IceCreamStand("Mobilice", "ice-cream")
# ice_cream_truck.display_flavours()

# ### 9.7 Admin

# class User:
#     """Class that contains user data"""
#     def __init__(self, first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.city = city.title()
#         self.occupation = occupation.title()
#         self.phone_number = phone_number
#         self.email_addess = email_address
#         self.hobby = hobby
#         self.music_genre = music_genre
#         self.sport = sport
#         self.favourite_food = favourite_food
#         self.login_attempts = 0

#     def describe_user(self):
#         """Displays all user information."""
#         print("\nUser details ")
#         print(f"Full name: {self.first_name} {self.last_name}")
#         print("User contact details ")
#         print(f"Cell: {self.phone_number} \tEmail: {self.email_addess}")
#         print("General information ")
#         print(f"{self.first_name} is a(n) {self.occupation} from {self.city}. He enjoys {self.hobby}, listening to {self.music_genre} music, watching {self.sport} and eating {self.favourite_food}.")

#     def greet_user(self):
#         """Displays a simple user greeting."""
#         print(f"Hello there {self.first_name}, how's the coding going?")

#     def increment_login(self):
#         """Increments login attempts."""
#         self.login_attempts += 1

#     def reset_logins(self):
#         self.login_attempts = 0

# class Admin(User):
#     """Represents a user with admin rights."""
#     def __init__(self, first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food):
#         """Initiates attributes from parent (user) class."""
#         super().__init__(first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food)
#         self.privileges = ["can add post", "can delete post", "can ban user", "can create user"]

#     def show_privileges(self):
#         """Prints privileges a user has."""
#         print("This user has the following privileges: ")
#         for right in self.privileges:
#             print(f"\t-{right}")

# my_user = Admin("khaya", "ubisi", "johannesburg", "software engineer", "0854569504", "k@something.co", "chess", "kpop", "soccer", "lasangne")

# my_user.show_privileges()

# ### 9.8 Privileges
# class User:
#     """Class that contains user data"""
#     def __init__(self, first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.city = city.title()
#         self.occupation = occupation.title()
#         self.phone_number = phone_number
#         self.email_addess = email_address
#         self.hobby = hobby
#         self.music_genre = music_genre
#         self.sport = sport
#         self.favourite_food = favourite_food
#         self.login_attempts = 0

#     def describe_user(self):
#         """Displays all user information."""
#         print("\nUser details ")
#         print(f"Full name: {self.first_name} {self.last_name}")
#         print("User contact details ")
#         print(f"Cell: {self.phone_number} \tEmail: {self.email_addess}")
#         print("General information ")
#         print(f"{self.first_name} is a(n) {self.occupation} from {self.city}. He enjoys {self.hobby}, listening to {self.music_genre} music, watching {self.sport} and eating {self.favourite_food}.")

#     def greet_user(self):
#         """Displays a simple user greeting."""
#         print(f"Hello there {self.first_name}, how's the coding going?")

#     def increment_login(self):
#         """Increments login attempts."""
#         self.login_attempts += 1

#     def reset_logins(self):
#         self.login_attempts = 0

# class Privileges:
#     """Represents user privileges."""
#     def __init__(self):
#         """Initialises privilege attributes"""
#         self.privileges = [
#             "can add post", 
#             "can delete post", 
#             "can ban user", 
#             "can create user"
#             ]
#     def show_privileges(self):
#         """Prints the privileges the user can action."""
#         print("This user has the following privileges: ")
#         for right in self.privileges:
#             print(f"\t-{right}")

# class Admin(User):
#     """Represents a user with admin rights."""
#     def __init__(self, first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food):
#         """Initiates attributes from parent (user) class."""
#         super().__init__(first_name, last_name, city, 
#                 occupation, phone_number, email_address,
#                 hobby, music_genre, sport, favourite_food)
#         self.privileges = Privileges()

# my_admin_user = Admin("khiga", "lethu", "springs", "software developer", "024567643", "khi@gha.com", "food", "dancehall", "darts", "pap")

# my_admin_user.privileges.show_privileges()

# ### 9.9 Battery Upgrade
# class Car:
#     """A simple representation of a car."""
#     def __init__(self, make, model, year):
#         """Initialises car attributes."""
#         self.make = make.title()
#         self.model = model.title()
#         self.year = year
#         self.odometer_reading = 0
#         self.gas_tank_size = 60
    
#     def get_description(self):
#         """Prints neatly formatted car description."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name

#     def read_odometer(self):
#         "Prints the car's current mileage."
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Sets the car's odometer reading to the value provided."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Odometer cannot be rolled back!")

#     def increment_odometer(self, miles):
#         "Increases odometer reading by value provided."
#         self.odometer_reading += miles

#     def fill_gas_tank(self):
#         self.gas_price = 18
#         """Prints the cost to fill the gas tank."""
#         print(f"It will cost {self.gas_tank_size * self.gas_price} to fill this tank.")

# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size=75):
#         """Initialises a battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Prints a description of the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Prints a statement about the range provided by the battery."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can got about {range} miles on a full charge.")

#     def upgrade_battery(self):
#         """Increase the battery if battery below 100 kWh."""
#         if self.battery_size < 100:
#             self.battery_size = 100


# class ElectricCar(Car):
#     """Represents aspects of a car specific to an electric car."""

#     def __init__ (self, make, model, year):
#         """Initiates attributes about the parent class."""
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def fill_gas_tank(self):
#         """Electric cars do not have gas tanks."""
#         print("This car doesn't have a gas tank to be filled.")

# my_electric_car = ElectricCar("smart", "cabriolet", 2012)
# print(my_electric_car.get_description())
# my_electric_car.battery.get_range()

# my_electric_car.battery.upgrade_battery()
# my_electric_car.battery.get_range()

# ### 9.10 Imported Restaurant

# from restaurant import Restaurant

# my_cafe = Restaurant("Khaya's Kota", "traditional township")
# my_cafe.describe_restaurant()
# my_cafe.set_number_served(25)
# print(my_cafe.number_served)

# ### 9.11 Imported Admin
# from admin import Admin

# my_admin_user = Admin("khaya", "lethu", "boksburg", "software developer", "0254569025", "my@email.com", "chess", "rock", "football", "spaghetti")

# my_admin_user.privileges.show_privileges()

# ### 9.12 Multiple Modules
# from privileges_and_admin import Admin

# my_multi_module_user = Admin("James", "GiantPeach", "Peachville", "farmer", "5552492", "peaches@giant.com", "eating fruit", "peach rock", "darts", "peaches and cream")

# my_multi_module_user.privileges.show_privileges()

# ### 9.13 Dice
# from random import randint

# class Dice:
#     """A representation of a dice."""
#     def __init__(self, value=6):
#         """Initialises attributes of a dice."""
#         self.sides = value

#     def roll_dice(self):
#         """Simulates the rolling of a dice."""
#         self.side_of_dice = randint(1, self.sides)
#         print(f"The dice is showing {self.side_of_dice}.")

# # my_dice = Dice()
# # my_dice.roll_dice()

# # my_dice = Dice(10)
# # my_dice.roll_dice()

# my_dice = Dice(20)
# my_dice.roll_dice()

### 9.14 Lottery

from random import randint, choice

lotto_numbers = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def play_lotto():
    for i in range(1, 11):
        current_int = randint(1, 49)
        lotto_numbers.append(current_int)

    for i in range(1,6):
        letter_position = randint(1,25)
        current_letter = alphabet[letter_position]
        lotto_numbers.append(current_letter)

# print("The winnin lotto characters are: ")
# for i in range(1, 5):
#     winning_char = choice(lotto_numbers)
#     print(f"\t{winning_char}")

### 9.15 Lottery analysis

from random import choice

my_ticket = []
winning_numbers = []

def generate_numbers(empty_list):
    numbers = list(range(1, 10))
    alphabets = ['A', 'B', 'C', 'D', 'E']
    for i in range(1, 5):
        current_number = choice(numbers)
        empty_list.append(current_number)
        numbers.remove(current_number)
    # sorted(empty_list)
    empty_list.sort()
    empty_list.append(choice(alphabets))
        
    print(empty_list)
    return empty_list

ticket = generate_numbers(my_ticket)
print("\n")
draw = generate_numbers(winning_numbers)

count = 1

while ticket != draw:
    count += 1
    draw = []
    draw = generate_numbers(draw)
print(f"Winner after {count} draws.")    

