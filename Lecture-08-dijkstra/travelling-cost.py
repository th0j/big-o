import queue

MAX = 505
distances = [-1] * MAX
graph = [[] for _ in range(MAX)]

class Node:
  def __init__(self, id, distance):
    self.id = id
    self.distance = distance

  def __lt__(self, other):
    return self.distance <= other.distance

def dijkstra(s):
  pq = queue.PriorityQueue()
  pq.put((Node(s, 0)))
  distances[s] = 0

  while pq.empty() == False:
    node = pq.get()

    for neighbor in graph[node.id]:
      if (node.distance + neighbor.distance < distances[neighbor.id]) or distances[neighbor.id] == -1:
        distances[neighbor.id] = node.distance + neighbor.distance
        pq.put(Node(neighbor.id, distances[neighbor.id]))

def read_graph(n):
  for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))

n = int(input())
read_graph(n)

u = int(input())
dijkstra(u)

q = int(input())

for i in range(q):
  v = int(input())
  if distances[v] != -1:
    print(distances[v])
  else:
    print('NO PATH')
