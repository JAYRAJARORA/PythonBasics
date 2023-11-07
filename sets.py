myset = set()

myset.add(1)
myset.add(2)
print(myset)
print(len(myset))

print(1 in myset)
print(3 in myset)

myset.remove(2)
print(myset)

print(set([1, 2, 3]))

myset = {i for i in range(0, 10, 2)}
print(myset)

mySet = set()
mySet.add((1, 2))
print(mySet)
