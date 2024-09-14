alien_0 = {'color': 'green', "points": 5}  # dictionary
alien_1 = {'color': 'yellow', "points": 10}
alien_2 = {'color': 'red', "points": 15}
aliens = [alien_0, alien_1, alien_2]  # nest dictionaries inside a list

for alien in aliens:
    print(alien)  # print dictionary keys values from list of dictionaries
print()

############################################################################
# make an empty list for storing aliens
aliens = []

# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first five aliens
alien_printed = 0
for alien in aliens[:5]:
    print(alien)
    alien_printed += 1
print(f'Number of aliens printed: {alien_printed}.')
# show how many aliens have been created in total
print(f'Total number of all aliens: {len(aliens)}.')
print()

# redefine the first 3 aliens if they are green
for alien in aliens[:3]:
    if alien['color'] == 'green':
        # alien['color'] = "yellow"
        # alien['speed'] = 'medium'
        # alien['points'] = 10
        alien.update({'color': 'yellow', 'speed': 'medium', 'points': 10})  # reduce above 3 lines to 1.

for alien in aliens[:5]:
    print(alien)
print(f'Total number of all aliens: {len(aliens)}.')
