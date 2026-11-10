p,t=map(int, input().split())
gr=[[] for _ in range(p)]
for _ in range(t):
  a,b,w=map(int, input().split())
  gr[a].append((b,w))
  gr[b].append((a,w))

distb=[float('inf')]*p
distb[0]=0
import heapq
q=[(0,0)]
while q:
  cd,c=heapq.heappop(q)
  if cd != distb[c]: continue
  for nxt, w in gr[c]:
    nd=cd+w
    if nd>=distb[nxt]: continue
    distb[nxt]=nd
    heapq.heappush(q,(nd,nxt))

diste=[float('inf')]*p
diste[p-1]=0
import heapq
q=[(0,p-1)]
while q:
  cd,c=heapq.heappop(q)
  if cd != diste[c]: continue
  for nxt, w in gr[c]:
    nd=cd+w
    if nd>=diste[nxt]: continue
    diste[nxt]=nd
    heapq.heappush(q,(nd,nxt))

bst=distb[p-1]
# print(bst)
tot=0
for i in range(p):
  v=gr[i]
  for vv,w in v:
    if distb[i]+w+diste[vv]==bst:
      tot+=w

print(2*tot)