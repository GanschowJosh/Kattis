from bisect import bisect_right
n,k=map(int, input().split())
shows=[]
for _ in range(n):
  a,b=map(int, input().split())
  shows.append((a,b))

shows.sort(key=lambda x: x[1])
avail=[0]*k
ot=0
for s,e in shows:
  best=bisect_right(avail, s)-1
  if best==-1: continue
  avail.pop(best)
  avail.append(e)
  ot+=1

print(ot)
