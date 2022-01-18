# Editing lists (changing, adding and removing elements)

# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# # Changing an element in the list
# motorcycles[0] = "ducati"
# # motorcycles[1] = "ducati"
# print(motorcycles)

# Adding elements to a list
# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# motorcycles.append("ducati")
# print(motorcycles)

# motorcycles = []

# print(motorcycles)

# motorcycles.append("honda")
# print(motorcycles)

# motorcycles.append("yamaha")
# print(motorcycles)

# motorcycles.append("suzuki")
# print(motorcycles)

# Inserting elements into a list
# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# motorcycles.insert(0, "ducati")
# print(motorcycles)

# motorcycles.insert(2, "ducati")
# print(motorcycles)

# Removing elements from a list
# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# # del motorcycles[0]
# del motorcycles[2]
# print(motorcycles)

# Removing elements using the pop() method
# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)

# last_owned = motorcycles.pop()
# print(f"The last motorcyle I owned was a {last_owned.title()}.")
# print(motorcycles)

# Popping elements from a list in any position using index position
# last_owned = motorcycles.pop(1)
# print(f"The first motorcyle I owned was a {last_owned.title()}.")
# print(motorcycles)

# Removing elements by value (unkown index/position)
# motorcycles = ["ducati", "honda", "yamaha", "suzuki"]
# print(motorcycles)

# motorcycles.remove("ducati")
# print(motorcycles)

# using a variable and removing variable from list still give access to the variable
## remove() METHOD ONLY DELETES THE FIRST OCCURENCE OF A VALUE, FOR DUPLICATE VALUES A LOOP WILL BE REQUIRED
# too_expensive = "ducati"
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")

# Indexing error
motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles[3])
print(motorcycles[-1])
