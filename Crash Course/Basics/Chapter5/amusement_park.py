### Elif statements
# age = 17

# if age < 4:
#     print("You may enter for free!")
# elif age < 18:
#     print("Your admission fee is $25.")
# else:
#     print("Your admission fee is $40.")

age = 75 #22 #2, #17

if age < 4:
    price = "free!"
elif age < 18:
    price = "$25"
elif age < 65:
    price = "$40"
else:
    price = "$20"

# alternative:
# elif age >= 65:
# price = $20 this final elif statment instead of an else (catch all) can improve data integrity by only accepting valid inputs.     

print(f"Your admission cost is {price}.")


### Scribble pad
# ages = [3, 17, 18, 26]

# for age in ages:
#     if age < 4:
#         print("You may enter for free!")
#     elif age < 18:
#         print("Your admission fee is $25.")
#     else:
#         print("Your admission fee is $40.")