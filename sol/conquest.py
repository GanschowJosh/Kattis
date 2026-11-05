n,m=map(int, input().split())
br=[[] for _ in range(n)]
for _ in range(m):
  a,b=map(int, input().split())
  a-=1
  b-=1
  br[a].append(b)
  br[b].append(a)
arm=[int(input()) for _ in range(n)]


import heapq
used=[False]*n
used[0]=True
sz=arm[0]
q=[] #army size, island
for v in br[0]:
  heapq.heappush(q,(arm[v],v))
while q:
  ca,ci=heapq.heappop(q)
  # print(ca,ci,sz)
  if ca >= sz or used[ci]: continue
  sz+=ca
  used[ci]=True
  for v in br[ci]:
    if used[v]: continue
    heapq.heappush(q,(arm[v],v))
print(sz)