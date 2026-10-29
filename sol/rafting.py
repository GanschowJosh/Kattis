from math import sqrt
dist = lambda x, y: sqrt(pow(x[0]-y[0],2)+pow(x[1]-y[1],2))
dot = lambda a,b: a[0]*b[0]+a[1]*b[1]
sub = lambda a,b: (a[0]-b[0],a[1]-b[1])
add = lambda a,b: (a[0]+b[0],a[1]+b[1])
clt = lambda a,b,c: (dot(sub(c,a),sub(b,a)))/(dot(sub(b,a),sub(b,a)))
scl = lambda t,a: (t*a[0],t*a[1])
t=int(input())
for _ in range(t):
  n=int(input())
  inner = list(tuple(map(int, input().split())) for _ in range(n))
  m=int(input())
  outer=list(tuple(map(int, input().split()))for _ in range(m))
  mn=10**10
  for i in range(n):
    ni=(i+1)%n
    a,b=inner[i],inner[ni]
    mnx=10**10
    for j in range(m):
      c=outer[j]
      u=max(0,min(1,clt(a,b,c)))
      p=add(a,scl(u,sub(b,a)))
      mnx=min(mnx,dist(p,c))
    mn=min(mn,mnx)
  for i in range(m):
    ni=(i+1)%m
    a,b=outer[i],outer[ni]
    mnx=10**10
    for j in range(n):
      c=inner[j]
      u=max(0,min(1,clt(a,b,c)))
      p=add(a,scl(u,sub(b,a)))
      mnx=min(mnx,dist(p,c))
    mn=min(mn,mnx)
  print(mn/2)
