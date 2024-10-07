# input city and state, call a function to add it to a dictionary and then add it to a list

locations = []


def city_state(city_name, state_name):
    """ Add City and State to a dictionary and then return it."""
    value = {'city': city_name, 'state': state_name}
    return value

location_city = input("Enter City: ")
location_state = input('Enter State: ')
while location_city != 'q':
    locations.append(city_state(location_city, location_state))
    print()
    location_city = input("Enter City ('q' to quit): ")
    if location_city.lower() == 'q':
        print()
        break
    location_state = input('Enter State: ')

for location in locations:
    print(f"{location['city']}, {location['state']}")

print(f'\n{locations}')

