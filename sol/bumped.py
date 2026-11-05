from collections import defaultdict
n,m,f,s,t=map(int, input().split())
rds=defaultdict(list)
for _ in range(m):
  i,j,c=map(int, input().split())
  rds[i].append((j,c))
  rds[j].append((i,c))

flts=defaultdict(list)
for _ in range(f):
  u,v=map(int, input().split())
  flts[u].append(v)

import heapq
bst=defaultdict(lambda: 10**10) #store (city, flight used): cost
bst[(s,1)] = 0
q=[(0,0,s)] #cost, flight used, city

while q:
  cc,fu,ccit=heapq.heappop(q)
  # print(cc,fu,ccit)
  if bst[ccit,fu] < cc: continue
  if ccit == t:
    print(cc)
    break
  for (v,w) in rds[ccit]:
    if bst[(v,fu)] < cc+w: continue
    bst[v,fu]=cc+w
    heapq.heappush(q,(cc+w,fu,v))
  if fu: continue
  for v in flts[ccit]:
    if bst[(v,1)] < cc: continue
    bst[v,1]=cc
    heapq.heappush(q,(cc,1,v))
