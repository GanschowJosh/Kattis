from collections import deque
n=int(input())
gr=[]
bst=[]
for _ in range(n):
  gr.append(list(map(int, input().split())))
  bst.append([10**10]*n)


q=deque([(0,0,0)])#curr x, y, time
bst[0][0]=0
while q:
  cx,cy,ct=q.popleft()
  # print(cx,cy,ct)
  ch=1+ct
  for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:
    nx,ny=dx+cx,dy+cy
    if 0 > nx or nx >= n or 0 > ny or ny >= n: continue
    nt=ct
    if gr[nx][ny] >= ch:
      nt+=(gr[nx][ny]-ch+1)
    if bst[nx][ny]<=nt: continue
    bst[nx][ny]=nt
    q.append((nx,ny,nt))
print(bst[n-1][n-1])