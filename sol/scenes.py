n,w,h=map(int, input().split())

mod=10**9+7

prev=[1]*(n+1)
for _ in range(w):
  print(prev)
  curr=[0]*(n+1)
  total=0
  for b in range(n+1):
    total+=prev[b]
    if b > h:
      total-=prev[b-h-1]
    total%=mod
    curr[b]=total
  prev=curr

print((prev[n]-(min(h,n//w)+1))%mod)