from math import ceil
n,k=map(int, input().split())

t=[int(input()) for _ in range(n)]

mx=1
l=0

for r in range(n):
  while t[r]-t[l] >= 1000:
    l+=1
  mx=max(mx, r-l+1)
print(ceil(mx/k))