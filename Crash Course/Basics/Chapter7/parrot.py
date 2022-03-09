# message = input("Tell me something, and I will repeat it back to you: \n")
# print(message)

### While loops

prompt = "Tell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "


message = ""
while message != "quit":
    message = input(prompt)
    print(message)