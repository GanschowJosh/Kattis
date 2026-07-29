from collections import defaultdict
c=int(input())


nds=[]
for i in range(c):
  k = int(input())
  for _ in range(k):
    n,d=map(int, input().split())
    nds.append((d,n,i))

nds.sort()

curr_holds = {}
days=defaultdict(int)

for d,n,c in nds:
  curr_holds[c]=n
  days[d]=sum(curr_holds.values())

for k,v in sorted(days.items()):
  print(v, end=" ")
  