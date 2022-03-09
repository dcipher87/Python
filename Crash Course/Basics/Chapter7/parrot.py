# message = input("Tell me something, and I will repeat it back to you: \n")
# print(message)

### While loops

# prompt = "Tell me something and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message) 
    
# # Keey a record of all user input in a list
# prompt = "Tell me something and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# messages = []

# message = ""
# while message != "quit":
#     message = input(prompt)
#     messages.append(message)
#     print(message) 
# print(messages)

### Using a flag

prompt = "Tell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message) 