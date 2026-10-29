import heapq
n,m=map(int, input().split())
arr=list(tuple(map(int, input().split())) for _ in range(n))

arr.sort()

gone=[]
pt=0
nd=0
for a,s in arr:
  while gone and gone[0] < a:
    heapq.heappop(gone)
  if pt == len(gone) or gone[pt]-m > a:
    nd+=1
  else:
    heapq.heappop(gone)
  heapq.heappush(gone, a+s+m)

print(len(arr)-nd)
