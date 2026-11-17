n,t=input().split()
n=int(n)
layers=[[(1,[])]]
for _ in range(n):
  curr=[]
  l=input().split()
  pt=0
  clpt=0
  for idx,i in enumerate(l):
    if i.isdigit():
      curr.append((int(i),[]))
      layers[-1][pt][1].append(('node',clpt))
      clpt+=1
    else:
      layers[-1][pt][1].append(0 if i == 'F' else 1)
    if len(layers[-1][pt][1])==layers[-1][pt][0]:pt+=1
  if _ < n-1: layers.append(curr)
# print(layers)

opp={
  'A':'O',
  'O':'A'
}

def ev(l):
  last=[]
  ct=[]
  for i in range(n-1,0,-1):
    if i % 2:
      curr = t
    else:
      curr=opp[t]
    ct=[]
    for nl,nds in l[i]:
      cct=[]
      for nd in nds:
        if type(nd) == tuple:
          cct.append(last[nd[1]])
        else:
          cct.append(nd)
      ct.append(int(all(cct) if curr=='A' else any(cct)))
    last=ct
  # print(last)

def subtree(level,node):
  if level % 2:
    ndt = t
  else:
    ndt=opp[t]
  children=layers[level][node][1]
  res=[]
  for ch in children:
    if isinstance(ch,tuple):
      res.append(subtree(level+1,ch[1]))
    else:
      res.append((ch,1))
  if ndt == 'A':
    v=all(r[0] for r in res)
    su=sum(int(not r[0]) for r in res) #num not set
    return (int(v),min(r[1] for r in res) if v else sum(r[1] for r in res if not r[0]))
  if ndt == 'O':
    an=any(r[0] for r in res)
    return (int(an),sum(r[1] for r in res if r[0]) if an else min(r[1] for r in res))

print(subtree(1,0)[1])
