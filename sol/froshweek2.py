n,m=map(int, input().split())
t=list(map(int, input().split()))
l=list(map(int, input().split()))

t.sort()
l.sort()

ptt=0
ptl=0
while ptt < len(t) and ptl < len(l):
  if t[ptt] <= l[ptl]:
    ptt+=1
    ptl+=1
  else:
    ptl+=1
print(ptt)
