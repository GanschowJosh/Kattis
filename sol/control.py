from collections import defaultdict
n=int(input())
rec=list(list(map(int, input().split()[1:])) for _ in range(n))

mx=max(max(r) for r in rec)
parent=list(range(mx+1))
sz=[1]*(mx+1)

def find(a):
  while parent[a] != a:
    a=parent[a]
  return a

def union(a,b):
  fa=find(a)
  fb=find(b)
  if fa==fb: return
  sz[fa]+=sz[fb]
  parent[fb]=fa

p=rec[0][0]
for r in rec[0][1:]:
  union(p,r)

g=1

for r in rec[1:]:
  # print(parent)
  #gather all roots, if sum of sizes of the roots is the same as size of current, it's a 
  # subset that can be reused
  rts=set()
  su=0
  for rr in r:
    prr=find(rr)
    if prr in rts: continue
    su+=sz[prr]
    rts.add(prr)
  if su!=len(r): continue
  p=r[0]
  for i in r[1:]:
    union(p,i)
  g+=1

print(g)