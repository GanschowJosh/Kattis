from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

f,s,g,u,d = map(int, input().split())

q = deque([(s,0)])
v = bytearray(f+1)
v[s]=1
while q:
  c,cnt = q.popleft()
  if c == g: print(str(cnt)+"\n"); exit()
  up = c+u
  if up <= f and v[up]==0:
    v[up]=1
    q.append((up,cnt+1))
  down = c-d
  if down > 0 and v[down]==0:
    v[down]=1
    q.append((down,cnt+1))
else:
  print("use the stairs\n")