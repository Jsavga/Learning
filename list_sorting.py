
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (f"{cars} Defined list.")
cars.sort()
print (f'{cars} order changed with "sort" inbuilt method (sort permanently changes the list order).')
cars.sort(reverse=True)
print (f"{cars} sort reversed. Since sort method was used this is now the defined list.\n")


cars = ['bmw', 'toyota', 'audi', 'subaru']
print (f"{cars} redefined list to new order for next part.")
cars.reverse()
print (f'{cars} the "reverse" method to reverse list order "without sorting". This change is permanent too.\n')

print (f'{sorted(cars)} "sorted" inbuilt function temporarily changes the order for output.')
print (f"{sorted(cars, reverse=True)} using sorted function to temp reverse-sort list.")
print (f"{cars} since sorted function is temporary, the original list order is retained.\n")



print ('''The above codings are where I first started understanding the difference between inbuilt methods
and inbuilt functions.
 
Inbuilt method usually appear after the variable (or list, etc.) with a 
period such as "cars.sort()" and they change the item premanently with the new value.

Inbuilt functions usually appear before the item with the item in brackets such as "sorted(cars)"
and pass the value while retaining the original value of the item in it's variable (or list, etc.).''')

