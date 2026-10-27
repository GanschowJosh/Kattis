from math import sqrt
def dist(a,b):
  return sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2))

n=int(input())
for _ in range(n):
  m=int(input())
  isl=[]
  for _ in range(m):
    x,y=map(float, input().split())
    isl.append((x,y))
  used=[False]*m
  best=[float('inf')]*m
  best[0]=0
  total=0
  for _ in range(m):
    curr=-1
    for v in range(m):
      if not used[v] and (curr == -1 or best[v]<best[curr]):
        curr=v
    used[curr]=True
    total+=best[curr]
    for nxt in range(m):
      if nxt == curr: continue
      w=dist(isl[curr],isl[nxt])
      if not used[nxt] and w < best[nxt]: best[nxt]=w
  print(total)
