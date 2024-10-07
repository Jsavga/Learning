# prevent a function from modifying a list using a slice [:] notation
# This instead passes a copy of the list instead of the list itself


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to complete_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that wer printed"""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models) # passing a slice to the function will use a copy of the list
show_completed_models(completed_models)
print(unprinted_designs) #original list still here