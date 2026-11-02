from bisect import bisect_left, bisect_right
class Fenwick:
  def __init__(self,n,arr=None):
    self.n=n
    self.bit=[0]*(n+1)
    if arr is not None:
      self.bit[1:]=arr
      for i in range(1,n+1):
        j=i+(i&-i)
        if j <= n: self.bit[j]+=self.bit[i]
  def add(self,i,value):
    i+=1
    while i <= self.n:
      self.bit[i]+=value
      i+=i&-i
  def prefix(self,r):
    ans=0
    while r > 0:
      ans+=self.bit[r]
      r-=r&-r
    return ans
  def query(self,l,r):
    return self.prefix(r)-self.prefix(l)
  def kth(self,k):
    pos=0
    step=1<<(self.n.bit_length()-1)
    while step:
      nxt=pos+step
      if nxt <= self.n and self.bit[nxt]<k:
        pos=nxt
        k-=self.bit[nxt]
      step//=2
    return pos

n,k=map(int, input().split())

intervals=[]
for _ in range(n):
  a,b=map(int, input().split())
  intervals.append((a,b))

ends=[float('-inf')]
ends+=sorted(set(b for a,b in intervals))
rank={x:i for i,x in enumerate(ends)}
free=Fenwick(len(ends))
free.add(0,k)
rooms=[[] for _ in ends]
rooms[0]=list(range(k))
count=0
for i in sorted(range(n), key=lambda i: intervals[i][1]):
  start,end=intervals[i]
  stop=bisect_right(ends,start)
  available=free.prefix(stop)
  if available==0: continue
  r=free.kth(available)
  room=rooms[r].pop()
  free.add(r,-1)
  r=rank[end]
  rooms[r].append(room)
  free.add(r,1)
  count+=1
print(count)