user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

for k, v in user_0.items():  # define two variables (k and v) to be equal to the keys:values in user_0
    print(f"Key: {k}")
    print(f"Value: {v}")
    print()
print()

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print()

print(favorite_languages.keys())  # prints the dictionary keys for favorite_languages
print(favorite_languages.values())  # prints the dictionary values for favorite_languages
print()

for name in favorite_languages.keys():  # sorts the list of keys into name "keys()" is optional
    print(name.title())
print()

# still using favorite_languages dictionary from above
friends = ['phil', 'sarah', 'erin']  # "list" of friends
for name in favorite_languages:  # looping by keys is the default so ".keys()" is optional
    print(f'Hi {name.title()}.')
    if name in friends:  # check to see if one of friends match dictionary key
        language = favorite_languages[name]
        print(f'\t{name.title()}, I see you love {language.title()}!')
print()

for name in friends:
    if name not in favorite_languages:  # check if friend is not in the favorite_languages dictionary
        print(f'{name.title()}, you need to take the language poll.')
    else:  # if fined is in the dictionary
        print(f'{name.title()} has took the poll.')
print()

for name in sorted(favorite_languages.keys()):  # sorts the keys in favorite_languages before going through them
    print(f'{name}')
print()

print('The following languages are in the dictionary:')
for language in favorite_languages.values():  # go through dictionary values instead of keys
    print(language)
print()

# set
print('The following languages are in the dictionary:')
for language in set(favorite_languages.values()):  # use "set" to remove duplicates
    print(language)
