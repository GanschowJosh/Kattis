from collections import defaultdict, deque
from functools import cache
n,m=map(int, input().split())

a=set()

hits = {}
children = defaultdict(list)
for _ in range(n):
  name=input()
  h,s=map(int, input().split())
  hits[name]=h
  a.add(name)
  ta=[]
  for _ in range(s):
    nm=input()
    a.add(nm)
    ta.append(nm)
  children[name].extend(ta)


reqd = {}
for name in a:
  if name in reqd: continue
  def dfs(i):
    if i in reqd: return reqd[i]
    reqd[i]=hits.get(i, 0)+sum(dfs(j) for j in children[i])
    return reqd[i]
  dfs(name)

t=0
for _ in range(m):
  name=input()
  num=int(input())
  t+=reqd[name]*num

print(t % (10**9 + 7))