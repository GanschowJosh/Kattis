n,m=map(int, input().split())
gr=[]
dist=[]
for _ in range(n):
  gr.append(bytearray(input(), 'ascii'))
  dist.append([-1]*m)

from collections import deque
q=deque()
for i in range(n):
  for j in range(m):
    if i == 0 or i == n-1 or j == 0 or j == m-1:
      q.append((i,j,1))
      continue
    if any(gr[ni][nj]==ord('-') for ni,nj in [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]): 
      q.append((i,j,1))

while q:
  ci,cj,cd=q.popleft()
  #print(ci,cj,cd)
  if dist[ci][cj] < cd and dist[ci][cj]!=-1: continue
  dist[ci][cj]=cd
  for di,dj in [(-1,0),(0,-1),(0,1),(1,0)]:
    ni,nj=di+ci,dj+cj
    #print((ni,nj,gr[ni][nj],dist[ni][nj]) if ni==nj==2 else None)
    if 0 > ni or ni >= n or 0 > nj or nj >= m: continue
    if dist[ni][nj] <= cd+1 and dist[ni][nj]!=-1: continue
    if gr[ni][nj]!=ord('X'): continue
    dist[ni][nj]=cd+1
    q.append((ni,nj,cd+1))

#for row in dist:
  #print(row)
print(max(max(row) for row in dist))
