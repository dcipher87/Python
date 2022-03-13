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