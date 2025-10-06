# mutable, unordered, unique items only

new_set = set() #empty set

new_set1 = {1,2,3,4,5,6,1,2,7}
print(new_set1)

new_set1.remove(1) #error is not found
print(new_set1)

new_set1.discard(8) # safe removal
print(new_set1)

new_set1.pop()
print(new_set1)

new_set1.clear()
print(new_set1)

new_set1.add(25)
print(new_set1)





