MAX = 1005
graph = [[] for _ in range(MAX)]
visited = [False] * MAX
distant = [-1] * MAX

# Adjacency List
def read_graph(m):
  for _ in range(m - 1):
    node_x, node_y = map(int, input().split())
    graph[node_x].append(node_y)
    graph[node_y].append(node_x)

def dfs(root):
  stack = []

  visited[root] = True
  distant[root] = 0
  stack.append(root)

  while len(stack):
    node = stack.pop()
    for node_related in (graph[node]):
      if not visited[node_related]:
        visited[node_related] = True
        stack.append(node_related)
        distant[node_related] = distant[node] + 1

n = int(input())
read_graph(n)
dfs(1)

q = int(input())
min_distant = n
min_country_id = n

for _ in range(q):
  country_id = int(input())

  if distant[country_id] < min_distant or (distant[country_id] == min_distant and country_id < min_country_id):
    min_distant = distant[country_id]
    min_country_id = country_id

print(min_country_id)

