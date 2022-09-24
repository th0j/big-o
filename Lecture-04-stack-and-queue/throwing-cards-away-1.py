import queue

n = int(input())

while n != 0:
  q = queue.Queue()

  for i in range(1, n + 1, 1):
    q.put(i)

  if q.qsize() > 1:
    print("Discarded cards:", end=" ")
  else:
    print("Discarded cards:")

  while q.qsize() > 1:
    if q.qsize() > 2:
      print(q.get(), end=", ")
    else:
      print(q.get())
    q.put(q.get())

  print("Remaining card:", q.queue[0])
  n = int(input())