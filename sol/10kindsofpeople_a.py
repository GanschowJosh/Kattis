from collections import deque
r,c=map(int, input().split())
gr=[]
for _ in range(r):
  gr.append(list(map(int, list(input()))))

comps=[[None for _ in range(c)] for _ in range(r)]

curr=0
for i in range(r):
  for j in range(c):
    if comps[i][j] is not None: continue
    q=deque([(i,j)])
    comps[i][j]=curr
    orig = gr[i][j]
    while q:
      ci,cj=q.popleft()
      for di, dj in [(-1,0),(0,-1),(0,1),(1,0)]:
        ni,nj=di+ci,dj+cj
        if 0 > ni or ni >= r or 0 > nj or nj >= c: continue
        if gr[ni][nj]!=orig: continue
        if comps[ni][nj] is not None: continue
        comps[ni][nj]=curr
        q.append((ni,nj))
    curr+=1
# print(comps)

for row in comps:
  print(row)

n=int(input())
for _ in range(n):
  r1,c1,r2,c2=map(int, input().split())
  r1-=1
  c1-=1
  r2-=1
  c2-=1
  if comps[r1][c1] != comps[r2][c2]:
    print('neither')
  elif gr[r1][c1] == 1:
    print('decimal')
  else:
    print('binary')