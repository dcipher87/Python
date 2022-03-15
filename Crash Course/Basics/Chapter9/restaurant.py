class Restaurant:
    """A simple restaurant class/model"""

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"{self.name} is a {self.cuisine_type} family restaurant.")

    def open_restaurant(self):
        """Confirms that the restaurant is open"""
        print(f"{self.name} is open untill 20:00.")

    def set_number_served(self, served_customers):
        self.number_served = served_customers
    
    def increment_number_served(self, customers_today):
        self.number_served += customers_today