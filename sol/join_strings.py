n=int(input())
root=0
tail=list(range(n))
next_string = [-1]*n
strings = []
for _ in range(n):
  strings.append(input())

for _ in range(n-1):
  a,b=map(int, input().split())
  a-=1
  b-=1
  next_string[tail[a]]=b
  tail[a]=tail[b]
  if root == b:
    root = a

import sys
while root != -1:
  sys.stdout.write(strings[root])
  root = next_string[root]
sys.stdout.write('\n')
