n=int(input())
pts=[]
v=[]
u=[]
w=[]
for _ in range(n):
  x,y,vv=map(int, input().split())
  pts.append((x,y,vv))
  v.append(vv)
  u.append(x+y)
  w.append(x-y)

def works(t):
  return max(u[i]-t*v[i] for i in range(n))<=min(u[i]+t*v[i] for i in range(n)) and max(w[i]-t*v[i] for i in range(n))<=min(w[i]+t*v[i] for i in range(n))

lo,hi=0,2000000000
for _ in range(60):
  mid=(lo+hi)/2
  if works(mid):
    hi=mid
  else:
    lo=mid
print(lo)