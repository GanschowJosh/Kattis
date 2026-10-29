from bisect import bisect_left
n,k=map(int, input().split())
acts=[]
for _ in range(n):
  s,f=map(int, input().split())
  acts.append((s,f))

acts.sort(key=lambda x: x[1])
avail=[0]*k
ot=0
for i in range(n):
  # print(avail)
  cs,ce=acts[i]
  best=bisect_left(avail,cs)-1
  if best == -1: continue
  # print(best, avail, cs)
  avail.pop(best)
  avail.append(ce)
  ot+=1

# print(good)
print(ot)