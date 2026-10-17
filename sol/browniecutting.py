from math import sqrt, ceil
from collections import defaultdict
n,k = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]

def cross(a,b):
  return a[0]*b[1]-a[1]*b[0]



p2=0
vis=bytearray(n)

nx=lambda x: (x+1)%n
pv=lambda x: (x-1+n)%n
def sign(x):
  if x < 0 : return -1
  if x == 0: return 0
  if x > 0 : return 1

def sub(x,y):
  return (x[0]-y[0],x[1]-y[1])


result=set()

def add(i):
  i,j=i
  i,j=min(i,j),max(i,j)
  result.add((i,j))

for p1 in range(n):
  
  base=(points[nx(p1)][0]-points[p1][0], points[nx(p1)][1]-points[p1][1])

  while (p1 == p2 or p2 == nx(p1) or sign(cross(base, sub(points[nx(p2)], points[p2]))) == sign(cross(base, sub(points[p2],points[pv(p2)])))):
    p2=nx(p2)

  if vis[p1]: continue
  vis[p1]=1

  add((p1,p2))
  add((nx(p1),p2))

  if cross(base,sub(points[nx(p2)],points[p2])) == 0:
    add((p1,nx(p2)))
    add((nx(p1),nx(p2)))
    vis[p2]=1

dx=-1
lengths=defaultdict(int)
for i,j in result:
  i,j=min(i,j),max(i,j)
  x,y=points[i]
  a,b=points[j]
  d=(x-a)**2+(y-b)**2
  if j != i+1 and not(i==0 and j == n-1):
    lengths[d]+=1
  if d > dx:
   dx=d


dx2 = sqrt(dx)*2
nc = ceil(k / dx2)

while 4*nc**2*dx < k**2:
  nc += 1
if nc > lengths[dx] and 4*nc**2*dx == k**2:
  nc += 1

print(nc)