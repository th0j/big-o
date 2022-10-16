import queue
test_case = int(input())

for i in range(test_case):
  q = queue.Queue()
  pq = queue.PriorityQueue()

  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  for i in range(n):
    q.put((i, array[i]))
    pq.put(-array[i])

  count = 0

  while not pq.empty():
    index, job = q.get()
    pq_job = -pq.get()

    if job == pq_job:
      count += 1
      if index == m: break
    else:
      q.put((index, job))
      pq.put(-pq_job)

  print(count)
