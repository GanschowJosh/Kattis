def find(p, parent):
  curr = p
  while curr != parent[curr]:
    curr=parent[curr]
  return curr

while True:
  try:
    n,m=map(int, input().split())
    id=list(range(n))
    point=n
    parent=list(range(n+m))
    sz=[1]*(n+m)
    sm=[i+1 for i in range(n+m)]
    for _ in range(m):
      inp=list(map(int, input().split()))
      if inp[0] == 1:
        p,q=inp[1],inp[2]
        p-=1
        q-=1
        fp = find(id[p], parent)
        fq = find(id[q], parent)
        if fq == fp:
          continue
        parent[fp]=fq
        sz[fq]+=sz[fp]
        sm[fq]+=sm[fp]
      if inp[0] == 2:
        p,q=inp[1],inp[2]
        p-=1
        q-=1
        fp = find(id[p], parent)
        fq = find(id[q], parent)
        if fq == fp: continue
        sz[fp]-=1
        sm[fp]-=(p+1)
        id[p]=point
        point+=1
        parent[id[p]]=fq
        sz[fq]+=1
        sm[fq]+=(p+1)
      if inp[0] == 3:
        p=inp[1]-1
        fp=find(id[p],parent)
        print(sz[fp],sm[fp])
  except EOFError:
    break