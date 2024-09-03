# Copying a list

my_foods = ['pizza', 'donut', 'pecan pie']
friends_foods = my_foods  # this copies one list to another keeping them linked together
other_friends_food = my_foods[:]  # this copies one list to another, but they are then separate list
print(my_foods)
print(f"{friends_foods} - copied my list to another just using =")
print(f"{other_friends_food} - copied my list to this one using a slice [:]")
print()
my_foods.append('coffe cake')
print("Added item to my list")
print(my_foods)
print(f"{friends_foods} - linked List.")
print(f"{other_friends_food} - unlinked List")

# Straight copying a List using: second_list = first_list
# keeps those two List linked and changes to one will appear in the other. Later changes to either affect both.
#
# Copying a List using a slice: second_list = first_list[:]
# makes a new list from the first. It is no longer linked, meaning that later changes to one will not affect the other.
