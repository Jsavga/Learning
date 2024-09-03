squares = []
i = 0

for value in range(1, 11):
    squares.append(value ** 2)
    print(f'The square of {i + 1} is {squares[i]}.')
    i += 1

print(f"{squares} \n")

# clear the values used above
squares = []
value = 0

# this accomplishes the same thing as the for loop and squares.append above in one line
# This is a "List Comprehension"
squares = [value ** 2 for value in range(1, 11)]
print(squares)
