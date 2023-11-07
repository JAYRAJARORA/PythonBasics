import heapq

print('min heap')
minHeap = []
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 0)
heapq.heappush(minHeap, 2)

print(minHeap)  # minimum always at index 0
while len(minHeap):
    print(heapq.heappop(minHeap))

print('max heap')
# to use max heaps, you have a work around using -1
maxHeap = []
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, 0)
heapq.heappush(maxHeap, -6)

print(-1 * maxHeap[0])
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

print('using heapify')
arr = [10, 2, 1, 4, 3]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))
