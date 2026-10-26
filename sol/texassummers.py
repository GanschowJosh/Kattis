n=int(input())
shade=[]
idx={}
for i in range(n):
  x,y=map(int, input().split())
  shade.append((x,y))
  idx[(x,y)]=i
start=tuple(map(int, input().split()))
end=tuple(map(int, input().split()))

shade.append(end)


import heapq
from collections import defaultdict

def dijkstra(start):
  dist=defaultdict(lambda: float('inf'))
  parent=defaultdict(lambda: -1)
  dist[start]=0
  parent[start]=0
  q=[(0,start)]
  while q:
    cd,c=heapq.heappop(q)
    if cd != dist[c]: continue
    for nxt in shade:
      nx,ny=nxt
      nd=cd+pow(c[0]-nx,2)+pow(c[1]-ny,2)
      # print(nd, nxt)
      if nd >= dist[nxt]: continue
      dist[nxt]=nd
      parent[nxt]=c
      heapq.heappush(q,(nd,nxt))
  return dist, parent

dist,parent=dijkstra(start)
curr=parent[end]
ot=[]
while curr!=start and curr!=-1:
  ot.append(idx[curr])
  curr=parent[curr]

print('\n'.join(map(str,reversed(ot))) if ot else '-')