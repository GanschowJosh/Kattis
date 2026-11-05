n,m=map(int, input().split())
gr=[[] for _ in range(n)]
for _ in range(m):
  a,b=map(int, input().split())
  a-=1
  b-=1
  gr[a].append(b)
  gr[b].append(a)


def tk(v):
  if used[v]:
    return False
  used[v]=True
  for to in gr[v%n]:
    if mt[to]==-1 or tk(mt[to]):
      mt[to]=v
      return True

mt=[-1]*n
used=[False]*n
for i in range(n):
  used=[False]*n
  tk(i)

if all(i!=-1 for i in mt):
  for i in range(n):
    print(mt[i]+1)
else:
  print('Impossible')