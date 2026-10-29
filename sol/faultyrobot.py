from collections import defaultdict, deque
n,m=map(int, input().split())
gr=defaultdict(list)
fgr=defaultdict(list)
for _ in range(m):
  a,b=map(int, input().split())
  if a > 0:
    gr[a].append(b)
  else:
    a=-a
    fgr[a].append(b)

q=deque([(1, False)])#node, bugged

seen={}
rest=set()
while q:
  cn, cb=q.popleft()
  if (cn,cb) in seen:
    continue
  seen[(cn,cb)]=True
  if cn not in fgr: 
    rest.add(cn)
  if not cb:
    for v in gr[cn]:
      q.append((v, True))
  for v in fgr[cn]:
    q.append((v,cb))

print(len(rest))