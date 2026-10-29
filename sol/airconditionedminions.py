n=int(input())
rgs=list(tuple(map(int, input().split())) for _ in range(n))

rgs.sort(key=lambda x: x[1])

ass=0
nm=0
while ass != (1<<n)-1:
  mn=10**10
  lst=None
  for i, (s,e) in enumerate(rgs):
    if ass&(1<<i): continue
    if e < mn:
      lst=i
      mn=e
  ass|=(1<<lst)
  for i, (s,e) in enumerate(rgs):
    if ass & (1<<i): continue
    if s <= mn: 
      ass |= (1<<i)
  nm+=1
print(nm)