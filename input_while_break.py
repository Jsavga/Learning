# using the input function

# Display a prompt and ask for input, then print it
message = input('Tell me something, I will repeat it back to you: ')
print(f'{message}\n')

prompt = 'If you share your name, then I can personalize the messages you see.'
prompt += '\nWhat is your first name? '
name = input(prompt)
print(f'Hello, {name.title()}!\n')

###### This will cause a crash if the input isn't a number. #####
prompt = "Enter a number and I'll tell you if it's even or odd: "
number_question = input(prompt)
answer = int(number_question)
if answer % 2 == 0:
    print(f'The number "{number_question}" is even.')
else:
    print(f'The number "{number_question}" is odd.')
print()

# This is one way of checking if input is a number without crashing.
# When I have learned more it would be better to define it as a function
# While True: is a simple way to always keep running, requiring something like a break statement to exit the loop
number_question = ""
while True:
    number_question = input("Please enter a number ")
    try:
        val = int(number_question)
        break
    except ValueError:
        try:
            val = float(number_question)
            break
        except ValueError:
            print("I'm sorry,", f'"{number_question.upper()}" is a string, not a number.')
print(f'You entered the number {val}, which is a {type(val)}')
