from collections import defaultdict
n,m=map(int, input().split())

occurs = defaultdict(int)

for i in range(1,n+1):
  for j in range(1,m+1):
    occurs[i+j]+=1

mx = max(occurs.values())
for k, v in occurs.items():
  if v == mx:
    print(k)
