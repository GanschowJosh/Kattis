from collections import deque
from array import array
import sys
input = sys.stdin.readline
out = sys.stdout.write

n,m=map(int, input().split())

gr=[bytearray(map(int,list(input().strip()))) for _ in range(n)]

#island=1,ocean=2,lake=0
def fill(i,j,val,tofill):
  g=gr
  q=deque([(i,j)])
  gr[i][j]=tofill
  while q:
    ci,cj=q.popleft()
    ni=ci-1
    if ni>=0 and g[ni][cj]==val:
      q.append((ni,cj))
      gr[ni][cj]=tofill
    ni=ci+1
    if ni<n and g[ni][cj]==val:
      q.append((ni,cj))
      gr[ni][cj]=tofill
    nj=cj-1
    if nj>=0 and g[ci][nj]==val:
      q.append((ci,nj))
      gr[ci][nj]=tofill
    nj=cj+1
    if nj<m and g[ci][nj]==val:
      q.append((ci,nj))
      gr[ci][nj]=tofill

#fill oceans
for i in range(n):
  for j in range(m):
    if i not in [0,n-1] and j not in [0,m-1]: continue
    if gr[i][j]!=0:continue
    fill(i,j,0,2)

#get the coastline
coast=0
for i in range(n):
  for j in range(m):
    if gr[i][j]!=1: continue
    ni=i-1
    if ni<0 or gr[ni][j]==2:coast+=1
    ni=i+1
    if ni>=n or gr[ni][j]==2:coast+=1
    nj=j-1
    if nj<0 or gr[i][nj]==2:coast+=1
    nj=j+1
    if nj>=m or gr[i][nj]==2:coast+=1
    #print(i,j,coast)
print(coast)