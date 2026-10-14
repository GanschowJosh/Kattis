import sys
input=sys.stdin.readline

n=int(input().strip())

strs=[]

for _ in range(n):
  strs.append(input().strip())

tail=list(range(n))
next=[-1]*n
root=0

for _ in range(n-1):
  a,b=map(int, input().strip().split())
  a-=1
  b-=1
  next[tail[a]]=b
  tail[a]=tail[b]
  root=a

#print(tail)

while root != -1:
  sys.stdout.write(strs[root])
  root=next[root]
