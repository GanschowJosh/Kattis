from collections import deque

def solve():
  # Step 1: Input parsing
  n, m = map(int, input().split())
  pages = list(map(int, input().split()))

  graph = [[] for _ in range(n)]  # Forward dependency graph
  reverse_graph = [[] for _ in range(n)]  # Reverse dependency graph
  indegree = [0] * n  # To track indegrees for topological sorting

  # Step 2: Construct the graphs from the dependencies
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)  # 0-indexed
    reverse_graph[b - 1].append(a - 1)
    indegree[b - 1] += 1

  # Step 3: Topological Sort to determine the order of processing
  topo_order = []
  queue = deque([i for i in range(n) if indegree[i] == 0])

  while queue:
    node = queue.popleft()
    topo_order.append(node)
    for neighbor in graph[node]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        queue.append(neighbor)

  # Step 4: Calculate total pages needed for each chapter including prerequisites
  total_pages = pages[:]  # Start with direct page counts

  for node in topo_order:
    for neighbor in graph[node]:
      total_pages[neighbor] += total_pages[node]

  # Step 5: Identify culminating chapters (those with no outgoing edges)
  culminating = [i for i in range(n) if not graph[i]]

  # Step 6: Function to get all prerequisites for a chapter
  def get_prerequisites(chap):
    visited = set()
    stack = [chap]
    while stack:
      node = stack.pop()
      if node in visited:
        continue
      visited.add(node)
      for prev in reverse_graph[node]:
        stack.append(prev)
    return visited

  # Step 7: Find the minimum pages required for any two culminating chapters
  min_pages = float('inf')

  for i in range(len(culminating)):
    for j in range(i + 1, len(culminating)):
      chap1 = culminating[i]
      chap2 = culminating[j]

      # Get prerequisites for both chapters
      visited1 = get_prerequisites(chap1)
      visited2 = get_prerequisites(chap2)

      # Calculate total pages including shared prerequisites
      shared = visited1 & visited2
      total = total_pages[chap1] + total_pages[chap2] - sum(pages[k] for k in shared)

      # Update the minimum pages found
      min_pages = min(min_pages, total)

  # Step 8: Output the minimum number of pages required
  print(min_pages)

# Start the solution
solve()