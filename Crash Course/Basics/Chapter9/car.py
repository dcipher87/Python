"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name of car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Prints a statement showing car's current mileage."""
        print(f"The car currently has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Updates odometer reading to value provided if above current mileage"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer can't be rolled back.")

    def increment_odometer(self, miles):
        """Increase odometer reading by value provided."""
        self.odometer_reading += miles

# class Battery:
#     """A simple representation of an electric car battery."""

#     def __init__(self, battery_size=75):
#         """Initialise battery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Prints a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}_kWh battery.")

#     def get_range(self):
#         """Prints a statement about the range this battery provides."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315

#         print(f"This car can about {range} miles on a full charge.")

# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         """
#         Initialises attributes of parent (Car).
#         Then initialises attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()

        