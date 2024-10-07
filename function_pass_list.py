# passing a list to a function

def greet_users(names):
    """Print a sample greeting to each person in a list"""
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)


usernames = ['hannah', 'ralph', 'betty', 'walter']
greet_users(usernames)