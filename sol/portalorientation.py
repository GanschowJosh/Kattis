from math import sqrt
N=int(input())
D=list(map(int,input().split()))


def prime_factors(n):
  pf=set()
  if n < 2: return pf
  if n%2==0: pf.add(2)
  while n%2==0:
    n//=2
  for i in range(3,int(sqrt(n))+1,2):
    if n%i==0: pf.add(i)
    while n%i==0:
      n//=i

  if n > 2:
    pf.add(n)
  return pf


active={}
zero_start=None
best=-1
bestco=None

for i,num in enumerate(D):
  if num==0:
    if zero_start is None: zero_start=i
    if not active: continue
    start=min(active.values())
  elif num==1:
    active={}
    zero_start=None
    continue
  else:
    pf=prime_factors(num)
    fallback=zero_start if zero_start is not None else i
    active={p:active.get(p,fallback) for p in pf}
    zero_start=None
    start=min(active.values())

  if i-start > best:
    best=i-start
    bestco=start,i

if best == -1: print(-1)
elif best == 0: print(bestco[0])
else: print(*bestco)
