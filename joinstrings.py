import sys
input=sys.stdin.readline
N=int(input())
strings=[input().strip() for _ in range(N)]
next_string=[-1]*N
tail=list(range(N))
root=0
for _ in range(N-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  next_string[tail[a]]=b
  tail[a]=tail[b]
  root=a

answer=[]
while root!=-1:
  answer.append(strings[root])
  root=next_string[root]
sys.stdout.write("".join(answer))
