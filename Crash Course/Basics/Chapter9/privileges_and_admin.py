"""Class depicting an admin user and privileges."""
from user import User

class Privileges:
    """Represents user privileges."""
    def __init__(self):
        """Initialises privilege attributes"""
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can create user"
            ]
    def show_privileges(self):
        """Prints the privileges the user can action."""
        print("This user has the following privileges: ")
        for right in self.privileges:
            print(f"\t-{right}")

class Admin(User):
    """Represents a user with admin rights."""
    def __init__(self, first_name, last_name, city, 
                occupation, phone_number, email_address,
                hobby, music_genre, sport, favourite_food):
        """Initiates attributes from parent (user) class."""
        super().__init__(first_name, last_name, city, 
                occupation, phone_number, email_address,
                hobby, music_genre, sport, favourite_food)
        self.privileges = Privileges()