t=int(input())
for _ in range(t):
  n,m=map(int, input().split())
  needed = set((i,i+1) for i in range(1,n))
  bad=False
  for __ in range(m):
    a,b=map(int, input().split())
    if a > b: 
      bad=True
    needed.discard((a,b))
  if not bad:
    print(len(needed))
  else:
    print(-1)
