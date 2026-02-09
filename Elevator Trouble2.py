from collections import deque
from array import array
f,s,g,u,d = map(int, input().split())

vis = array('I')
s-=1
g-=1
q=deque([(s,0)])
while q:
  c,cnt=q.popleft()
  if c==g:print(cnt);exit()
  up = c+u
  if up < f and not vis[up]:
    q.append((up,cnt+1))
    vis[up]=1
  down=c-d
  if down>=0 and not vis[down]:
    q.append((down,cnt+1))
    vis[down]=1
print("use the stairs")