# start with users that need to be verified,
# and an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users
# move each user into list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Verifying user: {current_user.title()}')  # simulate verifying user
    confirmed_users.append(current_user)

confirmed_users.sort()  # sort method is permanent change

# display all confirmed users
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print()

##########################################
# remove items from a list with while loop

pets = ['dog', 'cat', 'dog', 'rabbit', 'cat', 'goldfish', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')  # remove method is permanent change

print(sorted(pets))  # sorted function is temporary change
print(pets)
