import sys
import math
out = sys.stdout.write
n,k,p=map(int, input().split())

ot=[]
for i in range(1,math.floor(math.sqrt(n))+1):
  # print(i)
  if n%i != 0: continue
  if i <= p and n // i <= k:
    ot.append(n//i)
  if n // i == i: continue
  if n // i <= p and i <= k:
    ot.append(i)
  

print(len(ot))

for o in sorted(ot):
  out(f'{o}\n')