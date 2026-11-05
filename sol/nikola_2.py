n=int(input())
fee=[None]+[int(input()) for _ in range(n)]

from collections import deque,defaultdict
import heapq

bst=defaultdict(lambda: 10**10)
mn=10**10
q=[(fee[2],2,1)] #total cost,square, last jump
while q:
  cc,cs,lj=heapq.heappop(q)
  # print(cs,cc,lj)
  if bst[cs,lj] < cc: continue
  if cs==n:
    mn=min(mn,cc)
    break
  bst[cs,lj]=cc
  ll=abs(lj)
  nxt=ll+1
  ns=cs+nxt
  if ns <= n and bst[ns,nxt] > cc+fee[ns]:
    bst[ns,nxt]=cc+fee[ns]
    heapq.heappush(q,((cc+fee[ns],ns,nxt)))
  nxt=-ll
  ns=cs+nxt
  if ns > 0 and bst[ns,nxt] > cc+fee[ns]:
    bst[ns,nxt]=cc+fee[ns]
    heapq.heappush(q,(cc+fee[ns],ns,nxt))
print(mn)

