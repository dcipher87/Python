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

    def get_description(self):
        "Return a neatly formatted descriptive name."
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

my_car = Car("Volkswagen", "Polo GT", 2012)

print(my_car.get_description())