from array import array
import sys
input=sys.stdin.readline
out=sys.stdout.write

ZERO=ord('0')
ONE=ord('1')
TWO=ord('2')

n,m=map(int, input().split())
gr=[bytearray(input().strip(),'ascii') for _ in range(n)] #0=non-ocean water,1=land,2=ocean

def fill(x,y):
  g=gr
  g[x][y]=TWO #marking ocean
  stack=[(x,y)]
  while stack:
    cx,cy=stack.pop()
    nx=cx-1
    if nx >= 0 and g[nx][cy]==ZERO:
      g[nx][cy]=TWO
      stack.append((nx,cy))
    nx=cx+1
    if nx < n and g[nx][cy]==ZERO:
      g[nx][cy]=TWO
      stack.append((nx,cy))
    ny=cy-1
    if ny >= 0 and g[cx][ny]==ZERO:
      g[cx][ny]=TWO
      stack.append((cx,ny))
    ny=cy+1
    if ny < m and g[cx][ny]==ZERO:
      g[cx][ny]=TWO
      stack.append((cx,ny))

for i in range(n):
  if gr[i][0]==ZERO:fill(i,0)
  if gr[i][m-1]==ZERO:fill(i,m-1)
for i in range(m):
  if gr[0][i]==ZERO:fill(0,i)
  if gr[n-1][i]==ZERO:fill(n-1,i)

# for row in gr:
#   print(row)

count = 0
for i in range(n):
  for j in range(m):
    c=gr[i][j]
    if c!=ONE:continue
    ci=i-1
    if ci < 0 or gr[ci][j]==TWO:
      count+=1
    ci=i+1
    if ci>=n or gr[ci][j]==TWO:
      count+=1
    cj=j-1
    if cj < 0 or gr[i][cj]==TWO:
      count+=1
    cj=j+1
    if cj>=m or gr[i][cj]==TWO:
      count+=1

print(count)
