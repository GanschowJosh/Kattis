n=int(input())
r1=list(map(int, input().split()))
r2=list(map(int, input().split()))

def feas(w):
  l=None
  for i in r1:
    if i <= w: continue
    if l == None:
      l=i
      continue
    if i!=l:
      return False
    if i == l:
      l=None
  if l is not None:
    return False
  for i in r2:
    if i <= w: continue
    if l == None:
      l=i
      continue
    if i!=l:
      return False
    if i==l:
      l=None
  return l is None

l,r=0,max(max(r1),max(r2))+1
while l < r:
  mid=(l+r)//2
  if feas(mid):
    r=mid
  else:
    l=mid+1
print(l)