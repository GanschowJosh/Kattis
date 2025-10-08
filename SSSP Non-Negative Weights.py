import heapq
from collections import defaultdict
import sys

def dijkstra(graph, start, n):
  distances = [float('inf')] * n
  distances[start] = 0
  pq = [(0, start)]

  while pq:
    currdist, currnode = heapq.heappop(pq)

    if currdist > distances[currnode]:
      continue
  
    for neighbor, weight in graph[currnode]:
      distance = currdist + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))
      
  return distances

while True:
  n, m, q, s = list(map(int, input().split()))
  if n == m == q == s == 0:
    break

  graph = defaultdict(list)
  for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
  distances = dijkstra(graph, s, n)

  for _ in range(q):
    target = int(input())
    if distances[target] == float('inf'):
      print("Impossible")
    else:
      print(distances[target])

  print()