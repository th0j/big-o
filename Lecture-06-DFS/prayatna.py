
MAX = 100005
graph = [[] for _ in range(MAX)]
visited = [False] * MAX

# Adjacency List
def read_graph(m):
  for _ in range(m):
    node_x, node_y = map(int, input().split())
    graph[node_x].append(node_y)
    graph[node_y].append(node_x)

def dfs(root):
  stack = []

  visited[root] = True
  stack.append(root)

  while len(stack) > 0:
    node = stack.pop()
    for node_realated in graph[node]:
      if not visited[node_realated]:
        visited[node_realated] = True
        stack.append(node_realated)

t = int(input())
for _ in range(t):
  n = int(input())
  # Reset
  graph = [[] for _ in range(MAX)]
  visited = [False] * MAX

  e = int(input())
  read_graph(e)

  count = 0
  for i in range(n):
    if visited[i] == False:
      dfs(i)
      count += 1
  print(count)