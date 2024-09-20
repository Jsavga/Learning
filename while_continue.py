# "continue" in a while loop will skip the code after it and jump ack to the start

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # skips any following code and goes back to the while start condition check
    print(current_number)
