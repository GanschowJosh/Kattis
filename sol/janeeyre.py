import heapq
import re
n,m,k=map(int, input().split())

jire="Jane Eyre"
bks=[]
for _ in range(n):
  ma=re.fullmatch(r'"([^"]*)" (.+)', input().strip())
  t,p=ma.groups()
  if t>jire: continue
  heapq.heappush(bks, (t,int(p)))
  
heapq.heappush(bks, ("Jane Eyre", k))

received=[]
for _ in range(m):
  ma=re.fullmatch(r'(.+?) "([^"]*)" (.+)', input().strip())
  t,ti,l=ma.groups()
  if ti>jire: continue
  received.append((int(t),ti,int(l)))

received.sort()

curr=0
nrec=0
read=False
while bks:
  cb=heapq.heappop(bks)
  # print(cb, curr)
  curr+=cb[1]
  if cb[0]==jire:
    break
  while nrec < len(received) and received[nrec][0]<=curr:
    r=received[nrec]
    heapq.heappush(bks, (r[1], r[2]))
    nrec+=1
  

print(curr)
