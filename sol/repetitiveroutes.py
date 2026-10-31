n=int(input())
pick={}
last={}
bit=[0]*(2*n+1)

def update(i,delta):
  while i < len(bit):
    bit[i]+=delta
    i+=i&-i
def query(i):
  total=0
  while i:
    total+=bit[i]
    i-=i&-i
  return total


comp=0
for i in range(1, 2*n+1):
  c,t=map(int, input().split())
  comp+=query(last.get(t,0))
  if c not in pick:
    pick[c]=i
    update(i,1)  
  else:
    update(pick[c],-1)
    del pick[c]
  last[t]=i
  
print(comp)