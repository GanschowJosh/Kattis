from collections import deque, defaultdict
import heapq
n=int(input())

costs=[0]
for _ in range(n):
  costs.append(int(input()))
#costs.extend(list(int(input()) for _ in range(n)))

bst=defaultdict(lambda: 10**10)

q=[(costs[2], 2, 1)] #cost, curr square, last jump

optimal=10**10

while q:
  cd,cs,lj=heapq.heappop(q)
  #print(cd,cs,lj)
  if cd > bst[(cs, lj)]: continue
  #print(cs, lj, cd)
  if cs == n:
    optimal=min(optimal, cd)
    break
  if cs+lj+1 <= n:
    if bst[(cs+lj+1,lj+1)] > cd+costs[cs+lj+1]:
      bst[(cs+lj+1,lj+1)]=cd+costs[cs+lj+1]
      heapq.heappush(q,(cd+costs[cs+lj+1], cs+lj+1, lj+1))
  if cs-lj >= 1:
    if bst[(cs-lj, lj)] > cd+costs[cs-lj]:
      bst[(cs-lj, lj)]=cd+costs[cs-lj]
      heapq.heappush(q,(cd+costs[cs-lj],cs-lj,lj))

print(optimal)