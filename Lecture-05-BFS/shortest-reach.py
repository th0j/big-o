import queue

MAX = 1005
EDGE = 6
visited = [False] * MAX
distant = [-1] * MAX
graph = [[] for i in range(MAX)]

def read_graph(m):
  # Init graph base on Adjacency List method: Adjacency Matrix + Edge List
  for i in range(m):
    node_x, node_y = map(int, input().split())
    graph[node_x].append(node_y)
    graph[node_y].append(node_x)

def bfs(s):
  q = queue.Queue()
  visited[s] = True
  distant[s] = 0
  q.put(s)

  while q.qsize() > 0:
    node = q.get()

    for node_related in graph[node]:
      if visited[node_related] == False:
        visited[node_related] = True
        distant[node_related] = distant[node] + 1
        q.put(node_related)

q = int(input())

for j in range(q):
  # Reset
  visited = [False] * MAX
  distant = [-1] * MAX
  graph = [[] for i in range(MAX)]
  n, m = map(int, input().split())
  read_graph(m)

  s = int(input())
  bfs(s)

  for i in range(1, n + 1):
    if s != i:
      if i == n: print(max(distant[i] * EDGE, -1), end='\n')
      else: print(max(distant[i] * EDGE, -1), end=' ')