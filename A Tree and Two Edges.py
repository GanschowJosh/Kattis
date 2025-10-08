"""import networkx as nx

g = nx.Graph()
n, q = list(map(int, input().split()))
g.add_nodes_from(i for i in range(1, n+1))
for _ in range(n+1):
  u, v = map(int, input().split())
  g.add_edge(u, v)
for _ in range(q):
  u, v = map(int, input().split())
  paths = list(nx.all_simple_paths(g, u, v))
  print(len(paths))"""

#without external modules: 
################################# Iterative DFS Verdict: TLE
"""
def dfsCount(graph, start, end):
  stack = [(start, {start})] #(current node, visited nodes)
  path_count = 0
  
  while stack:
    current, visited = stack.pop()

    if current == end:
      path_count += 1
      continue
    
    for neighbor in graph[current]:
      if neighbor not in visited:
        newvisited = visited.copy()
        newvisited.add(neighbor)
        stack.append((neighbor, newvisited))
  
  return path_count

n, q = list(map(int, input().split()))
graph = {i: [] for i in range(1, n+1)}

for _ in range(n+1):
  u, v = list(map(int, input().split()))
  graph[u].append(v)
  graph[v].append(u)

for _ in range(q):
  u, v = list(map(int, input().split()))
  pathcount = dfsCount(graph, u, v)
  print(pathcount)
"""