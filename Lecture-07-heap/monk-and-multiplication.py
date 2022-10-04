import heapq

class MaxHeap:
  def __init__(self, value):
    self.value = value
  def __lt__(self, other):
    return self.value > other.value

n = int(input())
a = list(map(int, input().split()))

h = []

for i in range(n):
  heapq.heappush(h, MaxHeap(a[i]))

  if i < 2:
    print(-1)
  else:
    max_1 = heapq.heappop(h).value
    max_2 = heapq.heappop(h).value
    max_3 = heapq.heappop(h).value

    print(max_1 * max_2 * max_3)
    heapq.heappush(h, MaxHeap(max_1))
    heapq.heappush(h, MaxHeap(max_2))
    heapq.heappush(h, MaxHeap(max_3))
