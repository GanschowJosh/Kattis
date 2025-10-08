from collections import defaultdict, deque


def check(a, b):
  if a == b:
    return True
  visited = set()
  queue = deque([a])
  while queue:
    current = queue.popleft()
    if current == b:
      return True
    for neighbor in translations[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  return False

translations = defaultdict(set)
m, n = map(int, input().split())

for i in range(m):
  a, b = input().split()
  translations[a].add(b)

results = []
for i in range(n):
  a, b = input().split()
  if len(a) != len(b):
    results.append('no')
    continue
  match = True
  for c1, c2 in zip(a, b):
    if not check(c1, c2):
      match = False
      break
  results.append('yes' if match else 'no')

print('\n'.join(results))