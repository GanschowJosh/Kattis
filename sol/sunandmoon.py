ds,ys=map(int, input().split())
dm,ym=map(int, input().split())

def egcd(a,b):
  x,y,nx,ny=1,0,0,1
  while b:
    q=a//b
    a,b=b,a-q*b
    x,nx=nx,x-q*nx
    y,ny=ny,y-q*ny
  if a < 0: a,x=-a,-x,-y
  return a,x,y

eq=[(-ds%(ys),ys),(-dm%(ym),ym)]

x,m=0,1
for a, n in eq:
  g,inv,_=egcd(m,n)
  step=((a-x)//g*inv)%(n//g)
  x+=m*step
  m*=n//g
  x%=m
print(x)