import heapq

n, channels, B = map(int, input().split())

twins = []
for _ in range(n):
  left, right = sorted(map(int, input().split()))
  twins.append((left, right))

twins.sort()
active_ends = []

for left, right in twins:
  while active_ends and active_ends[0] < left:
    heapq.heappop(active_ends)

  heapq.heappush(active_ends, right + B)

  if len(active_ends) > channels:
    print("impossible")
    break
else:
  print("possible")