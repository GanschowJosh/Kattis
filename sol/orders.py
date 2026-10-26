n=int(input())
menu=list(map(int, input().split()))
m=int(input())
orders=list(map(int, input().split()))

from collections import defaultdict, deque
seen=defaultdict(int)
parent=defaultdict(lambda: -1)
mx=max(orders)

seen[0]=1


for i,item in enumerate(menu):
  for s in range(item, mx+1):
    if seen[s] == 0 and seen[s-item] > 0:
      parent[s]=i
    seen[s]=min(2,seen[s]+seen[s-item])

for order in orders:
  if seen[order] == 0:
    print('Impossible')
  elif seen[order] == 2:
    print('Ambiguous')
  else:
    ot=[]
    curr=order
    while curr > 0:
      i=parent[curr]
      ot.append(i+1)
      curr -= menu[i]
    print(*sorted(ot))