from collections import defaultdict
n=int(input())

seen=defaultdict(int)
seen[0]=1
parent=defaultdict(lambda: -1)
for bill in [1,5,15,30,150]:
  for i in range(bill, n+1):
    if seen[i-bill]>0:
      parent[i]=bill
    seen[i]+=seen[i-bill]

# print(parent)
need=defaultdict(int)
while n != 0:
  need[parent[n]]+=1
  n-=parent[n]
for i in [1,5,15,30,150]:
  print(need[i],end=' ')