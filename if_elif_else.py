# if - else  evaluates and does one or the other

age = 17
if age >= 18:
    print('You are old enough to vote')
else:
    print("you're not old enough to vote.")

# if - elif -else  evaluates until one passes, exits the rest of the loop if one does
age = 12
# admission price is different for 0-3, 4-17, 18-64, 65 and older
if age < 4:
    print('Your admission is $0.')
elif age < 18:
    print('Your admission is $15.')
elif age < 65:
    print('your admission is $25.')
else:
    print('Your admission is $10.')

# if - elif -else  repeat above more concise
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 15
elif age < 65:
    price = 25
else:
    price = 10
print(f'Your admission is ${price}.')
