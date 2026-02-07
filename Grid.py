from collections import deque
from array import array
import sys
input = sys.stdin.readline
out = sys.stdout.write

n,m=map(int, input().split())

g=[bytearray(map(int, list(input().strip()))) for _ in range(n)]
v=[bytearray(m) for _ in range(n)]
si,sj=(0,0)
q = deque([(si,sj,0)])
while q:
  i,j,c=q.popleft()
  #print(i,j)
  if i==(n-1) and j==(m-1):
    print(c)
    exit()
  k=g[i][j]
  ni=i-k
  if ni>=0 and v[ni][j]==0:
    v[ni][j]=1
    q.append((ni,j,c+1))
  ni=i+k
  if ni<n and v[ni][j]==0:
    v[ni][j]=1
    q.append((ni,j,c+1))
  nj=j-k
  if nj>=0 and v[i][nj]==0:
    v[i][nj]=1
    q.append((i,nj,c+1))
  nj=j+k
  if nj<m and v[i][nj]==0:
    v[i][nj]=1
    q.append((i,nj,c+1))
print(-1)