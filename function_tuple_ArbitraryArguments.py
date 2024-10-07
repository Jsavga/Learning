# use a tuple to pass an arbitrary number of arguments to a function
# this lets you pass a single value or multiple values to a function
# the asterisk in front of the parameter (*toppings) tells this function to use argument as a tupple

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""

    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')


make_pizza('cheese')
make_pizza('cheese', 'pepperoni', 'mushrooms')

# You'll often see the generic parameter name *args for functions that use arbitrary arguments
# for example, the above function could have been:
# def make_pizza(*args) to denote that it was being passed and arbitrary number of arguments
