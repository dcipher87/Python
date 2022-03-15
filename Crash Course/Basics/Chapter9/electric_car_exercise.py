# class Car:
#     """Simple representation of a car."""

#     def __init__(self, make, model, year):
#         self.make = make.title()
#         self.model = model.title()
#         self.year = year
#         self.odometer_reading = 0
#         self.gas_tank_size = 60

#     def get_description(self):
#         """Returns a long-name description of the car."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name

#     def read_odometer(self):
#         print(f"The car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Sets a new odometer reading if new reading > current reading."""
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("Odometer reading cannot be rolled back.")

#     def increment_odometer(self, miles):
#         """Increase the odometer reading by given value."""
#         self.odometer_reading += miles

#     def fill_gas_tank(self):
#         gas_price = 18
#         print(f"To fill this tank will cost: {self.gas_tank_size * gas_price}")

# class ElectricCar(Car):
#     """Represents aspects of a car, specific to electric cars."""
    
#     def __init__(self, make, model, year):
#         """
#         Initialises attributes of the parent class.
#         Then initialises attributes specific to an electric car.
#         """

#         super().__init__(make, model, year)
#         self.battery_size = 75

#     def describe_battery(self):
#         """Prints a statement describing the battery."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def fill_gas_tank(self):
#         """Electric cars do not have gas tanks."""
#         # print("This car does not have a gas tank.")
         
# # my_tesla = ElectricCar("tesla", "model s", 2019)
# # print(my_tesla.get_description())

# # my_tesla.describe_battery()

# my_car = Car("Honda", "Ballade", 1995)
# my_car.fill_gas_tank()

# my_tesla = ElectricCar("Tesla", "model t", 2020)
# my_tesla.fill_gas_tank()

### Instances as attributes ###

class Car:
    """A simple representation of a car."""
    def __init__(self, make, model, year):
        """Initialises car attributes."""
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_size = 60
    
    def get_description(self):
        """Prints neatly formatted car description."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        "Prints the car's current mileage."
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Sets the car's odometer reading to the value provided."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer cannot be rolled back!")

    def increment_odometer(self, miles):
        "Increases odometer reading by value provided."
        self.odometer_reading += miles

    def fill_gas_tank(self):
        self.gas_price = 18
        """Prints the cost to fill the gas tank."""
        print(f"It will cost {self.gas_tank_size * self.gas_price} to fill this tank.")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialises a battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a description of the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Prints a statement about the range provided by the battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can got about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represents aspects of a car specific to an electric car."""

    def __init__ (self, make, model, year):
        """Initiates attributes about the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car doesn't have a gas tank to be filled.")

my_electric_car = ElectricCar("tesla", "model y", 2019)
print(my_electric_car.get_description())

#my_electric_car.battery.battery_size = 100
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()