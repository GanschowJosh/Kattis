from collections import defaultdict, deque
from functools import cache
t=int(input())
for _ in range(t):
  n=int(input())
  colors=list(input().split())
  m=int(input())
  bad=defaultdict(set)
  for _ in range(m):
    a,b=input().split()
    bad[a].add(b)
    bad[b].add(a)

  nxt=defaultdict(int)
  @cache
  def dfs(i, last, used):
    if i == n:
      return 1
    su=0
    fav=None
    for j,color in enumerate(colors):
      if color in bad[last]: continue
      if used & (1<<j): continue
      o=dfs(i+1,color,used|(1<<j))
      if o and fav is None:
        fav=color
        nxt[(last,used)]=j
      su+=o
    return su
  print(dfs(0,None,0))
  
  last=None
  used=0
  for _ in range(n):
    j=nxt[(last,used)]
    last=colors[j]
    print(last, end=' ')
    used |= (1<<j)

    