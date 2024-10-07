# Positional arguments in a defined function allow you to pass multiple arguments to a function
# if you just pass values, then order of values passed matters
#calling a function requires value to be passed for each argument unless it has a default value

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f'\nI have a {animal_type}.', end=' ')
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# pass arguments in order (order of values passed matters)
describe_pet('hamster', 'harry')
describe_pet('dog', 'lucky')

# pass arguments using keyword/value pairs. Order passed doesn't matter but the Keywords must match exact
# names of parameters in function

describe_pet(pet_name='wally', animal_type='fish')
describe_pet(animal_type='cat', pet_name='dixie')

#use a default value for one of the parameters
# change order for function so that pet name is first.
# This way if you pass only one argument, it's the pets name and the second argument defaults to dog
def describe_pet_default(pet_name, animal_type='dog'):
    """Display info about a pet, pet type default if not passed is 'dog'  """
    print(f'\nI have a {animal_type}.', end=' ')
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_default('willie')  # this will pass name and use default for animal type
describe_pet_default('eddie','monkey') #over-rides default animal type
describe_pet_default(animal_type='frog', pet_name='waldo')  # can still use keyword value
