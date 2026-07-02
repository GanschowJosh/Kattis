n,t=map(int, input().split())
p=[]
for _ in range(n):
  p.append(int(input()))

ans=0
for mask in range(1, 1<<n):
  prod=1
  bits=0

  for i in range(n):
    if mask>>i & 1:
      prod*=p[i]
      bits+=1
      if prod>t:
        break

  if prod>t: continue

  if bits%2==1:
    ans+=t//prod
  else:
    ans-=t//prod

print(ans)