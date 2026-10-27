from collections import defaultdict
n=int(input())
gr={}
for _ in range(n):
  it=input()
  gr[it]=set()
m=int(input())
for _ in range(m):
  a,b=input().split()
  gr[a].add(b)
  gr[b].add(a)


color=defaultdict(lambda: -1)
grp=[[]for _ in range(2)]
for u in gr.keys():
  if color[u]!=-1: continue
  color[u]=0
  grp[0].append(u)
  stack=[u]
  while stack:
    curr=stack.pop()
    for nxt in gr[curr]:
      if color[nxt] == -1:
        color[nxt]=1-color[curr]
        grp[color[nxt]].append(nxt)
        stack.append(nxt)
      elif color[nxt]==color[curr]:
        print('impossible')
        exit()

print(' '.join(grp[0]))
print(' '.join(grp[1]))
