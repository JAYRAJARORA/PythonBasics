# arrays

arr = [1, 2, 3]

print(arr)

arr.append(4)
arr.append(5)

print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr2 = [3, 4, 5]
print(arr2[-1])
print(arr2[-2])

# print(arr2[-5]) - index out of range
print('Slicing')
arr = [1, 3, 4, 5, 6]
print(arr[1:3])

print(arr[0:4])
print(arr[0:10])

nums = [4, 6, 8, 10]
for n in nums:
    print(n)
for i in range(len(nums)):
    print(f'The index is {i} and number is {nums[i]}')

for i, n in enumerate(nums):
    print(i, n)

print('zip')
nums1 = [2, 3, 4, 5]
nums2 = [8, 9, 10, 11]
for num1, num2 in zip(nums1, nums2):
    print(num1, num2)

keys = ['a', 'b', 'c']
values = [1, 2, 3]

print(dict(zip(keys, values)))

nums2.reverse()
print(nums2)

arr = [10, 4, 2, 11]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ['alice', 'bob', 'jane', 'does not']
arr.sort()
print(arr)

arr.sort(key=lambda x: len(x), reverse=True)
print(arr)

arr = [2, 4, 6, 8]
list1 = [i*i for i in arr]
list2 = [i // 2 for i in arr if i % 4 == 0]
print(list1)
print(list2)

arr = [[i] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])

my_list = [1, 2, 3, 4, 5]

print('enumeration to modify the list')
for index, value in enumerate(my_list):
    my_list[index] = value * 2

print(my_list)