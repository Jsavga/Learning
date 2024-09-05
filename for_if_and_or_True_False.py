# if statements
# == check whether items are same
# != check whether items are not the same

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':  # checks if items match (equals)
        print(car.upper())  # if True then prints item in all uppercase
    else:
        print(car.title())  # otherwise prints item with Title case
    # 'for' loops here until ( for car in cars: ) is finished.

print()  # lack of indention means for loop is over so program can continue

age1 = 22
age2 = 18

if (age1 >= 21) and (age2 >= 21):  # check if all conditions are true
    print("Everyone is at least 21")

if (age1 >= 21) or (age2 >= 21):  # check is some conditions are true
    print('At least one person 21 or over')

if (age1 >= 25) or (age2 >= 25):
    print('At least one person 25 or older')

# evaluate expressions and print True or False from outcome
print((age1 >= 21) and (age2 >= 21), (age1 >= 21) or (age2 >= 21), (age1 >= 25) and (age2 >= 25))
print(age1 != age2)
