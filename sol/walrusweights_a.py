from collections import deque, defaultdict

n=int(input())
pl=list(int(input()) for _ in range(n))

targ=1000
q=deque([(0,0)])
best=0
seen=set()

while q:
  cp,cw=q.popleft()
  if (abs(targ-best),-best) > (abs(targ-cw),-cw):
    best=cw
  if cp==n: continue
  if (cp+1,cw+pl[cp]) not in seen:
    q.append((cp+1,cw+pl[cp]))
  if (cp+1,cw) not in seen:
    q.append((cp+1,cw))

print(best)