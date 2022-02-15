cars = ["audi", "bmw", "subaru", "toyota"]

# Prints BMW in upper case, all other car makes in title case
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# car = "audi"
# print(car=="audi") # evaluates to true


# Testing for equality is case sensetive Python
# car = "Audi"
# print(car=="audi") # evaluates to false

# Convert variables to lower case before comparison 
car = "Audi"
print(car.lower()== "audi") # .lower method does not change the value originally stored
print(car)