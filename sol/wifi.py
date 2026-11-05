t=int(input())
for _ in range(t):
  n,m=map(int, input().split())
  houses=[int(input()) for _ in range(m)]
  houses.sort()
  def feas(r):
    curr=r+houses[0]
    pt=1
    ct=1
    while pt < len(houses):
      if houses[pt] <= curr:
        pt+=1
        continue
      else:
        curr=houses[pt]+r
        ct+=1
        pt+=1
    return ct <= n
  l,r=0,houses[-1]
  while l < r:
    mid=(l+r)//2
    if feas(mid):
      r=mid
    else:
      l=mid+1
  print(f"{l/2:.1f}")