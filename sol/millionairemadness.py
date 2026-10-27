from collections import deque
import heapq
m,n=map(int, input().split())
gr=[]
bst=[]
for _ in range(m):
  gr.append(list(map(int, input().split())))
  bst.append([10**10 for _ in range(n)])

bst[0][0]=0

q=[(0,0,0)]#max jump,x,y

while q:
  mj,cx,cy=heapq.heappop(q)
  cgr=gr[cx][cy]
  if mj != bst[cx][cy]: continue
  if cx == m-1 and cy == n-1: break
  for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
    nx,ny=cx+dx,cy+dy
    if 0 > nx or nx >= m or 0 > ny or ny >= n: continue
    ngr=gr[nx][ny]
    if ngr < cgr or mj >= ngr-cgr:
      df=0
    else:
      df=ngr-cgr-mj
    if bst[nx][ny] <= mj+df: continue
    bst[nx][ny]=mj+df
    heapq.heappush(q,(mj+df,nx,ny))

print(bst[m-1][n-1])
