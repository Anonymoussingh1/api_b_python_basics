# ordered, mutable, allows duplicates


mylist = [1,2,3,4,5]

# slicing a list
print(f"Start only {mylist[2:]}")
print(f"Only stop {mylist[:5]}") # stop before index 2
print(f"Start and Stop {mylist[2:5]}")

print(mylist)
print(type(mylist))

# insert - insert at a specific index
mylist.insert(0, 64)
print(mylist)

thelist = [1,2,3,4,5]
print(thelist)

def insert_at_index(thelist, index, value):
    thelist.insert(index, value)
    print(thelist)

insert_at_index(thelist, 2, 789)

# append - adding elements to the end
thelist.append(147)
print(thelist)

# get values
print(thelist[1])
print(thelist[-1])

thelist.pop()
print(thelist)

thelist.pop(3)
print(thelist)






