# Get the users wanted username, then send it to a function, and then return a formatted username

def username_format(i):
    """format a username to remove all whitespace and convert to lowercase"""

    user_name = "".join(i.split()).lower()
    return user_name


wanted_username = input('What username would you like: ')  # gets username that user wants
username = username_format(wanted_username)  # sends it to function which formats it and returns it
print(f'This is what it will look like after formating: {username}\n')


# Using a dictionary in a function and a list to contain the dictionaries
musicians = []
def build_person(first_name, last_name):
    """Return a dictionary of information about a person """

    person = {'first': first_name, 'last' : last_name}
    return person

musician = build_person('jimi', 'hendrix')
musicians.append(musician)
print(musician)
musician = build_person('don', 'henley')
musicians.append(musician)
print (musician)
print (musicians)

