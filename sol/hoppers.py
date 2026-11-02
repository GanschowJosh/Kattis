n,m=map(int, input().split())
gr=[[] for _ in range(n)]
for _ in range(m):
  u,v=map(int, input().split())
  u-=1
  v-=1
  gr[u].append(v)
  gr[v].append(u)

color=[-1]*n
comp=0
need=0
for start in range(n):
  if color[start]!=-1:continue
  good=False
  comp+=1
  color[start]=0
  stack=[start]
  while stack:
    curr=stack.pop()
    for nxt in gr[curr]:
      if color[nxt]==-1:
        color[nxt]=1-color[curr]
        stack.append(nxt)
      elif color[nxt]==color[curr]:
        good=True
  if not good:
    need+=1

print(comp-1+(need==comp))

