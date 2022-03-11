# ### Positional arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about pet"""
#     print(f"I have a {animal_type}.")
#     print(f"My pet {animal_type}'s name is {pet_name.title()}.\n")


# # describe_pet("dog", "dixie")
# # describe_pet("hamster", "harry")

# # describe_pet("harry", "hamster")

# ### Keyword arguments

# describe_pet(animal_type="snake", pet_name="Ka")
# describe_pet(animal_type="tegu", pet_name="stripes")

# # These function calls are equivalent
# describe_pet(animal_type="hamster", pet_name="harry")
# describe_pet(pet_name="Harry", animal_type="hamster")

### Default values

def describe_pet(pet_name, animal_type = "dog"):
    """Display information about a pet"""
    print(f"\nI have a pet {animal_type}.")
    print(f"My pet {animal_type}'s name is {pet_name.title()}.")

# describe_pet("Dixie")

# describe_pet("Earth Worm Jim", "snake")
# describe_pet(animal_type="snake", pet_name = "Earth worm jim")

# ### Equivalent function calls
# describe_pet("Dixie")
# describe_pet(pet_name = "Dixie")

# describe_pet("harry", "hamster")
# describe_pet(pet_name="harry", animal_type="hamster")    
# describe_pet(animal_type="hamster", pet_name="harry")

#describe_pet() # too few arguments
#escribe_pet("spike", "cat", 8) # too many arguments