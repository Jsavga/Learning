#use "in" and "not in"

requested_topping = 'mushrooms'
requested_toppings = ['mushrooms', 'onions', 'pineapple']

if requested_topping != "anchovies":  # checks inequality (not-equal). if items don't match then expression is True
    print('Hold the anchovies')  # if expression != is true then prints
print()

answer = 'mushrooms' in requested_toppings  # returns True or False
print(answer)
answer = 'pepperoni' in requested_toppings
print(answer)

bad_people = ['andrew', 'john', 'fred', 'caroline']
person = "marie"

if person not in bad_people:   #checks "not in"
    print (f'{person.title()} is good.')

person = "john"

if person in bad_people:  #checks "in"
    print (f'{person.title()} is bad.')