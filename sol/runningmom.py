from collections import defaultdict
n=int(input())
gr=defaultdict(list)
for _ in range(n):
  a,b=input().split()
  gr[a].append(b)

def dfs(curr,seen):
  if curr in seen:
    return True
  return any(dfs(i,seen.union({curr})) for i in gr[curr])

while True:
  try:
    c=input()
    print(c, 'safe' if dfs(c,set()) else 'trapped')
  except EOFError:
    break