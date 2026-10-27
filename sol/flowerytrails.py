import heapq
from collections import defaultdict

p,t=map(int, input().split())
graph=defaultdict(list)
for _ in range(t):
  p1,p2,l=map(int, input().split())
  graph[p1].append((p2,l))
  graph[p2].append((p1,l))

ds=[float('inf')]*p
ps=[-1]*p
ds[0]=0
ps[0]=0
q=[(0,0)]
while q:
  cd,c=heapq.heappop(q)
  if cd != ds[c]: continue
  for v,w in graph[c]:
    nd=cd+w
    if nd>=ds[v]: continue
    ds[v]=nd
    ps[v]=c
    heapq.heappush(q,(nd,v))

de=[float('inf')]*p
pe=[-1]*p
de[-1]=0
pe[-1]=p-1
q=[(0,p-1)]
while q:
  cd,c=heapq.heappop(q)
  if cd != de[c]: continue
  for v,w in graph[c]:
    nd=cd+w
    if nd>=de[v]: continue
    de[v]=nd
    pe[v]=c
    heapq.heappush(q,(nd,v))


# print(ds,de)

su=0
for u,v in graph.items():
  for vv, w in v:
    if ds[u]+w+de[vv]==ds[p-1] or ds[vv]+w+de[u]==ds[p-1]:
      su+=w

print(su)