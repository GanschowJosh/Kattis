from collections import defaultdict,deque
c,p,x,l=map(int, input().split())
gr=defaultdict(set)
num=defaultdict(int)
for _ in range(p):
  a,b=map(int, input().split())
  gr[a].add(b)
  gr[b].add(a)
  num[a]+=1
  num[b]+=1

gone=set()
q=deque([(l,None)])
seen=set()
num[l]=0

#print(num)

while q:
  curr,fr=q.popleft()
  if curr in gone: continue
  if (curr,fr) in seen: continue
  seen.add((curr,fr))
  num[curr]-=1
  s=len(gr[curr])
  if num[curr] <= s / 2:
    gone.add(curr)
    for v in gr[curr]:
      q.append((v,curr))
#print(gone)
print('stay' if x not in gone else 'leave')