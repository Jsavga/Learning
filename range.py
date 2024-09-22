#range() inbuilt function

# create a list from 0-9 (when no start value given it starts at 0)
# also note that end value is always 1 before (end value will equal 9 below)
rng = range(10)

print(rng)
print(list(rng))  # converts the rng iterator to a lists and prints it

rng = range(2, 10)  # adds a start value, now list is 2-9
print(list(rng))

rng = range(2, 10, 2)  # third parameter is the step value, since "end" value is always "1 before" it stops before 10
print(list(rng))

rng = range(10, -10, -2)  # start at 10 and subtract 2 for each step, note end value is still 1 before reaching -10
print(list(rng))

for i in range(0, 100, 5):
    print(i)
    i += i
