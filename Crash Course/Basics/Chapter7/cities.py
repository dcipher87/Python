# ### Using break to exit a loop

# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == "quit":
#         break #quits the loop
#     else:
#         print(f"I'd love to got to {city.title()}!")

### Using continue in a loop
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # if current_number % != 0 #for even numbers
        continue
    print(current_number)