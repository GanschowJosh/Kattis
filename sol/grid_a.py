from collections import deque
n,m=map(int, input().split())
gr=[]
for _ in range(n):
  gr.append(list(map(int, list(input()))))

bst=[[-1]*m for _ in range(n)]
bst[0][0]=0
q=deque([(0,0,0)])
while q:
  ci,cj,cd=q.popleft()
  # print(ci,cj,cd)
  curr=gr[ci][cj]
  for di, dj in [(-curr,0),(curr,0),(0,-curr),(0,curr)]:
    ni,nj=di+ci,dj+cj
    # print(ni,nj)
    if 0 > ni or ni >= n or 0 > nj or nj >= m: continue
    if cd+1 >= bst[ni][nj] and bst[ni][nj]!=-1: continue
    bst[ni][nj]=cd+1
    q.append((ni,nj,cd+1))
print(bst[-1][-1])
