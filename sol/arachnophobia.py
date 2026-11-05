from collections import defaultdict, deque
n,m,T=map(int, input().split())
gr=defaultdict(list)
for _ in range(m):
  u,v,d=map(int, input().split())
  gr[u].append((v,d))
  gr[v].append((u,d))

# print(gr)
s,t=map(int, input().split())

sdist=defaultdict(lambda: 10**10)
spiders=set(map(int, input().split()[1:]))
for sloc in spiders:
  q=deque([(sloc,0)]) #loc, dist
  while q:
    cloc,d=q.popleft()
    if sdist[cloc] < d: continue
    sdist[cloc]=d
    for v,w in gr[cloc]:
      if sdist[v]<d+w: continue
      sdist[v]=d+w
      q.append((v,d+w))

# print(sdist)

import heapq

def feas(s,D):
  dist=defaultdict(lambda: float('inf'))
  dist[s]=0
  q=[(0,s)]
  while q:
    cd,c=heapq.heappop(q)
    if cd != dist[c]: continue
    for nxt,w in gr[c]:
      if sdist[nxt]<D: continue
      nd=cd+w
      if nd >= dist[nxt]: continue
      dist[nxt]=nd
      heapq.heappush(q,(nd,nxt))
  return dist[t]<=T

l,r=0,min(sdist[s],sdist[t])+1
while l < r:
  mid=(l+r) // 2
  if not feas(s,mid):
    r=mid
  else:
    l=mid+1
print(l-1)