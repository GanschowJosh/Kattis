import sys
from collections import deque
from array import array

cases=int(input())
for _ in range(cases):
  n,t=map(int, input().split())
  b=array('i',map(int, input().split()))

  dist=array('h', [-1])*(3600+1)
  dist[0]=0
  me,mp=float('inf'),None #minimum extra, minimum presses
  q=deque([0])#current time
  while q:
    ct=q.popleft()
    cp=dist[ct]
    if ct>=t:
      extra=ct-t
      if extra < me:
        me=extra
        mp=cp
      if extra==0:
        break
    for bp in b:
      nt=ct+bp
      if nt < 0:
        nt=0
      elif nt>3600:
        nt=3600
      if dist[nt]==-1:
        dist[nt]=cp+1
        q.append(nt)
  print(f"{mp} {me}")
