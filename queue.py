from collections import deque

queue = deque()
queue.append(1)
queue.append(2)

print(queue)

queue.popleft()

print(queue)

queue.appendleft('abc')

print(queue)

queue.pop()
print(queue)