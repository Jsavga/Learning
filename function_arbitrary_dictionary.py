#pass an arbitrary key/value arguments to a function as a dictionary
#this lets you pass a single key/value pair or multiple key/value pairs to a function
# the double asterisk in front of the parameter (**keyinfo) tells this function to use nonspecific keyword arguments

def information(x,y,**keyinfo):
    """Build a dictionary with keyword passed arguments"""

    print('\nThe following key/value pairs were passed to this function:')
    for key in keyinfo:
        print(f'Key - {'key'[x]}    Value -{y}')


information('shoe', 'nike', color='green', item='tree')
