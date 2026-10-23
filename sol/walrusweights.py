n=int(input())
plates=list(int(input()) for _ in range(n))

targ=1000
total=sum(plates)

seen={}
seen[0]=True
for p in plates:
  for s in range(2*targ, p-1, -1):
    if s-p in seen:
      seen[s]=True

best=min((s for s in range(2*targ+1, -1, -1) if s in seen and seen[s]), key=lambda s: abs(s-targ))
print(best)