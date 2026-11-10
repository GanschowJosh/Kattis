d=int(input())
rows=[[] for _ in range(4)]
for _ in range(d):
  curr=list(map(int,input().split()))
  for i,c in enumerate(curr):
    rows[i].append(c)


from collections import deque,defaultdict

bst={} #col, component tuple

best=0

def all_set(mask):
  while mask:
    low=mask&-mask
    yield low.bit_length()-1
    mask^=low

q=deque([(0,0,('-','-','-','-'),0)]) #column, mined mask, components, mined
while q:
  cc, last_mined, comps, mined_total =q.popleft()
  if cc == d: continue
  labels = set(comps[i] for i in range(4) if comps[i] != '-')
  if bst.get((cc-1, comps),-1) > mined_total: continue
  for i in range(1<<4):
    curr_mined=set(all_set(i))
    bad_share=False
    for a,b in [(0,1),(1,2),(2,3)]:
      if last_mined&(1<<a) and last_mined&(1<<b) and i&(1<<a) and i&(1<<b): bad_share=True; break #overlap
    if bad_share: continue
    old_labels=set()
    for j in range(4):
      if last_mined&(1<<j) and i&(1<<j): old_labels.add(comps[j])
    if old_labels!=labels: continue #a component got cut off

    parent=list(range(4))
    def find(x):
      while x!=parent[x]:
        parent[x]=parent[parent[x]]
        x=parent[x]
      return x
    def union(a,b):
      a,b=find(a),find(b)
      if a == b: return
      parent[b]=a

    for j in range(4):
      if not i&(1<<j): continue
      for k in range(j+1,4):
        if not i&(1<<k): break
        union(j,k)
    first_bridge={}
    for j in all_set(last_mined&i):
      label=comps[j]
      union(first_bridge.setdefault(label,j),j)

    rtl={}
    next_comps=['-']*4
    for j in all_set(i):
      root=find(j)
      next_comps[j]=rtl.setdefault(root, len(rtl))
    next_comps=tuple(next_comps)
    
    curr_tot=mined_total
    for j in range(4):
      if i&(1<<j):
        curr_tot+=rows[j][cc]
    
    num_comps=len(rtl)
    if num_comps == 1:
      best=max(best, curr_tot)

    if bst.get((cc,next_comps),-1) >= curr_tot: continue
    bst[cc,next_comps] = curr_tot
    q.append((cc+1,i,next_comps,curr_tot))

print(f'Retrievable: {best}')
print(f'Remaining: {sum(map(sum,rows))-best}')