# while loops


# use a while loop to print 1 through 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Use a while loop to input text.
# check if the user input is "quit"
# if it's not then print the message and repeat
# if it is then skip printing it and exit
prompt = "\nTell me something and I'll repeat it back to you."
prompt += " (type 'quit' to end): "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
print()
