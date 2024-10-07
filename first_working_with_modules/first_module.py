# This is the function portion of previous codings so that I can learn use modules
# this function code with be imported as a module into another file.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""

    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')
