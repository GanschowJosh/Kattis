from collections import defaultdict
r,c=map(int, input().split())

gr=[]
for _ in range(r):
  gr.append(list(map(int, input().split())))

mxs=[]
mxf=[]
for i in range(r):
  mxs.append(max(gr[i]))
for j in range(c):
  mxf.append(max(gr[i][j] for i in range(r)))

conn=defaultdict(list)
for i in range(r):
  for j in range(c):
    if mxs[i]==mxf[j]>1 and gr[i][j]!=0:
      conn[i].append(j)

mt=[-1]*c
size=0
for i in range(r):
  used=[False]*r
  def tk(v):
    if used[v]: return False
    used[v]=True
    for u in conn[v]:
      if mt[u] == -1 or tk(mt[u]):
        mt[u]=v
        return True
    return False
  if tk(i):
    size+=1

tot=0
for i in range(r):
  for j in range(c):
    if gr[i][j] != 0: tot+=1

for i in range(r):
  tot+=max(0,mxs[i]-1)
for j in range(c):
  tot+=max(0,mxf[j]-1)

save=sum(mxf[col]-1 for col in range(c) if mt[col]!=-1)
tot-=save
print(sum(map(sum,gr))-tot)