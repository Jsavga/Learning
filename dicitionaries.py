# dictionaries use {key:value} pairs

color = 'red'
car = {'color': color}  # assign key-value pair to a dictionary in which key is 'color' and value is a variable
print(car['color'])  # print the value for the 'color' key

alien_0 = {'color': 'green', 'points': 7}  # assign 2 key-value pairs to a dictionary
print(alien_0['color'])
print(alien_0['points'])

# start with blank dictionary, add keys to it, remove keys from it and then modify keys in it
alien_0 = {}
alien_0['color'] = 'green'  # add key to dictionary
alien_0['points'] = 5
alien_0['size'] = 'medium'
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
del alien_0['points']  # removes a key-value pair from dictionary
print(alien_0)
alien_0['color'] = 'purple'  # modify an existing key's value in the dictionary
print(alien_0)

# .get method to check if key exist. Returns value only if it doesn't, otherwise returns dictionary key value
key_check = alien_0.get('points', "Doesn't exist")
print(key_check)  # 2nd argument assigned to variable key_check only if key doesn't exist in dicitionary
key_check = alien_0.get('color', "Doesn't exist")
print(key_check)  # since this key existed in dictionary, then value for variable was assigned from dictionary
key_check = alien_0.get('height')
print(key_check)  # if no 2nd argument is used, then "none" assigned to variable key_check if key doesn't exist
key_check = alien_0.get('size')
print(key_check)  # since key exist in dictionary, the dictionary key value is passed to the key_check variable
