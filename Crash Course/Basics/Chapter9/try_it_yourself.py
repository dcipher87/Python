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
