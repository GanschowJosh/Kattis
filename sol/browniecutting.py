from math import sqrt, ceil
from collections import defaultdict
n,k = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]

dx = -1
lengths = defaultdict(int)
for i, (x,y) in enumerate(points[:-1]):
  for j, (a,b) in enumerate(points[i+1:],i+1):
    d = (x-a)**2+(y-b)**2
    if j != i+1 and not (i == 0 and j == n-1):
      lengths[d] += 1
    if d > dx:
      dx = d


dx2 = sqrt(dx)*2
nc = ceil(k / dx2)

while nc > 0 and 4*(nc-1)**2*dx >= k**2:
  nc -= 1

while 4*nc**2*dx < k**2:
  nc += 1
if nc > lengths[dx] and 4*nc**2*dx == k**2:
  nc += 1

print(nc)