import heapq

n = int(input())

while ( n!=0 ):
  h = list(map(int, input().split()))
  heapq.heapify(h)

  cost = 0
  while len(h) > 1:
    sum = heapq.heappop(h) + heapq.heappop(h)
    heapq.heappush(h, sum)
    cost += sum

  print(cost)

  n = int(input())
