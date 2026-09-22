X=int(input())
N=int(input())
curr=0
for _ in range(N):
  curr += X
  i = int(input())
  curr -= i

print(curr+X)