# tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()

print('Originals dimensions:')
for dimension in dimensions:
    print(dimension)

print()

dimensions = (400, 100)  # can't change a tuple through a operation, but can reassign a tuple variable
print('Modified dimensions:')
for dimension in dimensions:
    print(dimension)
