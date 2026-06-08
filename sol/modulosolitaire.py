from collections import deque

m, n, s0 = map(int, input().split())

transformations = []
for _ in range(n):
  a, b = map(int, input().split())
  transformations.append((a, b))

queue = deque([(s0, 0)])
visited = set()
while queue:
  current_state, distance = queue.popleft()
  if current_state in visited:
    continue
  visited.add(current_state)

  if current_state == 0:
    print(distance)
    exit(0)

  for a, b in transformations:
    next_state = (current_state * a + b) % m
    queue.append((next_state, distance + 1))

print(-1)
