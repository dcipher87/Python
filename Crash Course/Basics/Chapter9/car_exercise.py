# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialises atrributes to describe car."""
#         self.make = make.title()
#         self.model = model.title()
#         self.year = year

#     def get_descriptive_name(self):
#         """Return neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name

# my_new_car = Car("audi", "a3", 2018)
# print(my_new_car.get_descriptive_name())

class Car:
    """A simple representation of a car."""

    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 10000

    def get_description(self):
        "Return a neatly formatted descriptive name."
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """Prints the car's mileage."""
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to value provided.
        Reject the change if it attempts to roll odometer back.
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add a given amount to odometer reading."""
        if miles > 0:
            self.odometer_reading = self.odometer_reading + miles
        else:
            print("Miles can only be a positive integer.")
        #self.odometer_reading += miles

# my_car = Car("Volkswagen", "Polo GT", 2012)

# print(my_car.get_description())
#my_car.read_odometer()

### Modifying attribute values

## Modifying an attributes value directly
# my_car.odometer_reading = 75

# my_car.read_odometer()

## Modifying an attribute value through a method

# my_car.read_odometer()
# my_car.update_odometer(500)
# my_car.read_odometer()

## Incrementing an attribute's value through a method
my_used_car = Car("subaru", "outback", 2015)
print(my_used_car.get_description())

my_used_car.update_odometer(24500)
my_used_car.read_odometer()

my_used_car.increment_odometer(500)
my_used_car.read_odometer()