from car import ElectricCar

my_electric_car = ElectricCar("tesla", "model s", 2018)
print(my_electric_car.get_descriptive_name())

print(my_electric_car.battery.battery_size)
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()