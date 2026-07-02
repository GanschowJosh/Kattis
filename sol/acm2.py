N,p=map(int, input().split())

probs=list(map(int, input().split()))
first=probs[p]

probs=probs[:p]+probs[p+1:]
probs.sort()
probs.insert(0, first)

curr=0
pen=0
c=0
for i in probs:
  curr+=i
  pen+=curr
  if curr > 300:
    pen-=curr
    break
  c+=1
print(c, pen)