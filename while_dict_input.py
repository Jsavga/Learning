responses = {}

# set a flag to indicate polling is active
polling_active = True

while polling_active:
    # prompt for person's name and response
    name = input('\nEnter your name: ')
    response = input('What is your favorite color: ')

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is taking the poll
    anyone_else = input('Would another person like to participate? (y/n)')
    if anyone_else == 'n':
        polling_active = False

# Polling is complete. Show the results
print('\n... Poll Results ...')
for name, response in responses.items():
    print(f'{name.title()} likes the color {response.title()}.')
