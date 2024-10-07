#pass differnt kinds of arguments to a function
# when using a tuple to pass an arbitrary number of arguments to a function mixed with other types of arguments,
# it must be last in the list. the (size) parameter is mixed with a tuple parameter in the example below.
# the asterisk in front of the parameter (*toppings) tells the function to use that argument as a tupple

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""

    print(f'\nMaking a {size.title()} pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza('large', 'cheese')
make_pizza('medium','cheese', 'pepperoni', 'mushrooms')
make_pizza('small', 'veggie')