n,t=map(int, input().split())
people=list(tuple(map(int, input().split())) for _ in range(n))
people.sort(reverse=True)

occ=[None]*t
tot=0

for c, tl in people:
  for m in range(min(tl, t-1),-1,-1):
    if occ[m] is None:
      occ[m]=c
      tot+=c
      break
print(tot)