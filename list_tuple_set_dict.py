# list   []
# tuple  ()
# set    {}
# dictionary {:}

names = ["mike", "john", "mary", "jill"]  # create a list
names2 = ["peter", "frank", "carl", "suzzie"]  # create a different list
names3 = []  # create an empty list
names4 = ("sally", "henry", "ward")  # create tuple (like a list that can't be changed)
names5 = {"jimmy", "todd", "wally", "fred"}  # create a set (set are un-ordered and unchangeable)
names_dict = {"user1": "tony", "user2": "helen", "user3": "lenny"}  # dictionary contains key-value pairs

# List
print(names)  # prints the entire list
print(len(names))  # lentgh function on a list shows how many "items" in the list
print(names[0], names[2])  # shows the first and third items in the list
print(names[0:3])  # shows a range of items of the list (0,1,2)
print(names[-2])  # shows the next to last item in the list (neg starts from last back)

names.append("douglas")  # appeands an item to the list
print(names)

names3.extend(names2)  # extend adds the items from one list to another list
names3.extend(names)
print(names3)

names3.insert(1, "tony")  # Inserts an item into a list at an index point
print(names3)

names3.remove("jill")  # remove first instance of a known string/value from the list
print(names3)
names3.pop(4)  # pop removes item from a list at index position (0,1,2,3,"4")
names3.pop()  # if left blank then it removes last index item from list
print(names3)  # from two lines above index item 4 and last index item are removed
del names3[2:4]  # Del can also remove items by index or slice
print(names3)
names3.clear()  # clears all items from the list
print(names3)

# tuple
print(names4)  # since this is a tuple the values in it can not be changed
# names4.remove("ward") would result in error since tuple is unchangeable
# tuples use () and must have at least one comma even if only one element (3,)

# set
print(names5)  # set may display different order each run.
num_set = {1, 5, 3, 5, 8, 7, 2, 5, 3}  # set also removes duplicates
print(num_set)

# dictionary
print(names_dict["user1"])  # dictionary use the key to print the value
print(names_dict["user3"])
# List is a collection which is ordered and changeable.Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable.Allows duplicate members.
# Set is a collection  which is unordered, *unchangeable*, and unindexed.No duplicate members.
#     *(can add and remove items to a set though)*
# Dictionary contains key-value pairs and uses the same {} as a set
