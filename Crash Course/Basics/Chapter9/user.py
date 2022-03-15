"""Class depicting our users."""

class User:
    """Class that contains user data"""
    def __init__(self, first_name, last_name, city, 
                occupation, phone_number, email_address,
                hobby, music_genre, sport, favourite_food):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.city = city.title()
        self.occupation = occupation.title()
        self.phone_number = phone_number
        self.email_addess = email_address
        self.hobby = hobby
        self.music_genre = music_genre
        self.sport = sport
        self.favourite_food = favourite_food
        self.login_attempts = 0

    def describe_user(self):
        """Displays all user information."""
        print("\nUser details ")
        print(f"Full name: {self.first_name} {self.last_name}")
        print("User contact details ")
        print(f"Cell: {self.phone_number} \tEmail: {self.email_addess}")
        print("General information ")
        print(f"{self.first_name} is a(n) {self.occupation} from {self.city}. He enjoys {self.hobby}, listening to {self.music_genre} music, watching {self.sport} and eating {self.favourite_food}.")

    def greet_user(self):
        """Displays a simple user greeting."""
        print(f"Hello there {self.first_name}, how's the coding going?")

    def increment_login(self):
        """Increments login attempts."""
        self.login_attempts += 1

    def reset_logins(self):
        self.login_attempts = 0
