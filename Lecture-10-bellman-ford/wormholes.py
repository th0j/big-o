import math

MAX = 2005

graph = []
dist = [math.inf] * MAX
path = [-1] * MAX

class Edge:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight

def bellman_ford(s):
  dist[s] = 0

  for _ in range(1, n):
    for i in range(m):
      u = graph[i].source
      v = graph[i].target
      w = graph[i].weight
      if dist[u] != math.inf and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        path[v] = u

  for i in range(m):
    u = graph[i].source
    v = graph[i].target
    w = graph[i].weight
    if dist[u] != math.inf and dist[u] + w < dist[v]:
      return False

  return True

c = int(input())
for _ in range(c):
  n, m = map(int, input().split())

  graph = []
  dist = [math.inf] * MAX
  path = [-1] * MAX

  for _ in range(m):
    u, v, w = map(int, input().split())
    graph.append(Edge(u, v, w))

  res = bellman_ford(0)

  if not res:
    print('possible')
  else:
    print('not possible')
