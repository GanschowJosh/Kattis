n=int(input())
gr=[]
for _ in range(n):
  gr.append(list(map(int, input().split())))

used=[False]*n
best=[float('inf')]*n
best[0]=0
parent=[-1]*n
for _ in range(n):
  curr = -1
  for v in range(n):
    if not used[v] and (curr == -1 or best[v]<best[curr]):
      curr=v
  used[curr]=True
  if parent[curr]!=-1:
    print(parent[curr]+1,curr+1)
  for nxt,w in enumerate(gr[curr]):
    if not used[nxt] and w < best[nxt]: 
      best[nxt] = w
      parent[nxt]=curr
