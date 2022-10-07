import heapq

q = int(input())

h = []
deleted = {}

for i in range(q):
  queries = list(map(int, input().split()))
  action, value = (queries[0], queries[1] if len(queries) > 1 else None)

  if action == 1:
    heapq.heappush(h, value)
  elif action == 2:
    if value in deleted: deleted[value] += 1
    else: deleted[value] = 1
  else:
    while True:
      min_heap = h[0]
      if min_heap in deleted:
        heapq.heappop(h)
        deleted[min_heap] -= 1
        if deleted[min_heap] <= 0: del(deleted[min_heap])
      else: break
    print(min_heap)
