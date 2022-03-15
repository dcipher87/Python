from car import Car

my_new_car = Car("audi", "a3", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 3563
my_new_car.read_odometer()