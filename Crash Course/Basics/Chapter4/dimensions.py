dimensions = (200, 50)

# print(dimensions[0])
# print(dimensions[1])

# dimensions[1] = 100 # error when trying to change the value of a tuple value
# print(dimensions)

# for dime in dimensions:
#     print(dime)

print("Original dimensions:")
for dime in dimensions:
    print(dime)

dimensions = (400, 100)
print("\nModified dimensions:")
for dime in dimensions:
    print(dime)    