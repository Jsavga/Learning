requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print('\nFinished making your pizza.\n')

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print(f'Adding {requested_topping}')

print('\nFinished making your pizza.\n')

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Sorry, we are out of green peppers right now')
        else:
            print(f'Adding {requested_topping}')
else:
    print('\nFinished making your plain pizza is ready.\n')

available_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'olives'
                                                                    'pepperoni', 'pineapple']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print('\nFinished making your pizza.')
