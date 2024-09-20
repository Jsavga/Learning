# "while True:" will continue to run until you leave it by something like a break statement
# "break" will exit out of a loop, whether it's a while loop, a for loop, etc.
# "try" and "except" checks for an error and catches it instead of crashes if there is one.

# the following ask for a number, checks if it is a number and prints it and it's type
while True:
    b1 = input('Type a number:')
    try:
        a1 = int(b1)
        break
    except ValueError:
        try:
            a1 = float(b1)
            break
        except ValueError:
            print(f'"{b1}" is not a number. Try again.')
print(f'You typed the number {a1}, which is a {type(a1)}.')
