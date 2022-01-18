# Oganising a list

# ## Sorting a list permanently with sort()
# cars = ["bmw", "audi", "toyota", "subaru"]
# print(cars)
# cars.sort() # permanently sorted, cannot revert back to original list.
# print(cars)

# cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort(reverse=True)
# print(cars)

# # Sorting temporarily with the sorted() function
# cars = ["bmw", "audi", "toyota", "subaru"]

# print("Here is the original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))
# #print(sorted(cars, reverse=True)) # Sorted() can also accept reverse = True

# print("\nHere is the original list again:")
# print(cars)

# ##### SORTING LISTS ALPHABETICALLY IS MORE COMPLICATED WHEN ALL THE VALUES ARE NOT IN LOWERCASE #####

# ## Printing in reverse order
# cars = ["bmw", "audi", "toyota", "subaru"]
# print(cars)

# cars.reverse() #not backwards alphabetically, reverse of original order
# print(cars) #reverse() method is a permanent change, revers again or original order

#Finding the length of a list
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))