myMap = {}

myMap['alice'] = 'wonder'
myMap['harry'] = 'hogwards'

print(myMap)
print(len(myMap))

myMap['alice'] = 80
print(myMap)

myMap.pop('alice')
print('harry' in myMap)
print('alice' in myMap)

# dictionary comprehension
myMap = {i: i**3 for i in range(4)}
print(myMap)

myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

print('Using items')
for key, val in myMap.items():
    print(key, val)
