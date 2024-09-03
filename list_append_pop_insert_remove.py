motorcycles = ["honda", "yamaha", "suzuki", "kawasaki"]
print (motorcycles)

motorcycles[0] = "ducati"   #changes an element of the list at index position
print (motorcycles)
motorcycles.append("honda")   #adds elements to the end of a list
print (motorcycles)

motorcycles = []
print (motorcycles)
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print (motorcycles)
motorcycles.insert(0, "ducati")   #insert and element into the list at index pos
motorcycles.insert(2, "kawasaki")
print (motorcycles)
del motorcycles[0]   #deletes an items from list at index pos, doesn't retain it
print (motorcycles)
poppedmotorcycle = motorcycles.pop()   #delets item from list and reatains it for use in another variable
print (motorcycles)
print (poppedmotorcycle.title() + " was removed from the list")
motorcycles.remove("honda")   #removes item for the list that matches a known value (not an index pos)
print (motorcycles)
