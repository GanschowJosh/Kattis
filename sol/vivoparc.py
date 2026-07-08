from collections import deque
n=int(input())

sees=[set() for _ in range(n)]


while True:
  try:
    a,b=map(int, input().split("-"))
    a-=1
    b-=1
    sees[a].add(b)
    sees[b].add(a)
  except EOFError:
    break

assigned=[None for _ in range(n)]

def dfs():
  best=-1
  best_used=None

  for v in range(n):
    if assigned[v] is None:
      used = set(assigned[u] for u in sees[v] if assigned[u] is not None)
      if best==-1 or len(used) > best_used:
        best=v
        best_used=len(used)

  if best==-1: return True

  v=best
  used=set(assigned[u] for u in sees[v] if assigned[u] is not None)

  for c in range(1,5):
    if c not in used:
      assigned[v]=c
      if dfs():
        return True
      assigned[v]=None
  return False

dfs()

for i, ass in enumerate(assigned):
  print(f"{i+1} {ass}")