from math import factorial
t=int(input()) 
for _ in range(t):
  n=int(input())
  MOD=998244353
  fact=[1]*(n+1)
  for i in range(1,n+1):
    fact[i]=fact[i-1]*i%MOD
  blocks=[]
  for _ in range(n):
    blocks.append(tuple(map(int, input().split())))
  blocks.sort(key=lambda x: x[0]*x[1], reverse=True)
  from collections import defaultdict
  grps=defaultdict(set)
  sz=defaultdict(int)
  for bl,bw in blocks:
    mb=(min(bl,bw),max(bl,bw))
    grps[bl*bw].add(mb)
    sz[mb]+=1
  if any(len(v)>1 for v in grps.values()): 
    print(0)
    continue
  su=1
  mxl,mxw=(None,None)
  for k,v in sorted(grps.items(),reverse=True):
    vv=list(v)
    vv=vv[0]
    tim=0
    if mxl is not None:
      orientations = {vv,(vv[1],vv[0])}
      for l,w in orientations:
        if l <= mxl and w <= mxw:
          tim+=(mxw-w+1)*(mxl-l+1)
    if mxl is None:
      tim = 1 if vv[0]==vv[1] else 2
      mxl,mxw=vv
    mxl,mxw=vv
    su= su * fact[sz[vv]]*tim%MOD
  print(su)
  

