pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]

# numbers_of_cats = 0

# #counts number of cats as they are removed
# while "cat" in pets:
#     numbers_of_cats += 1
#     pets.remove("cat")
# print(numbers_of_cats)

while "cat" in pets:
    pets.remove("cat")

print(pets)