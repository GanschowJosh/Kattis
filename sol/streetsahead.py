n,q=map(int, input().split())
pt=0
d={}
for _ in range(n):
  c=input()
  d[c]=pt
  pt+=1

for _ in range(q):
  a,b=input().split()
  mx=max(d[a],d[b])
  mn=min(d[a],d[b])
  print(mx-mn-1)