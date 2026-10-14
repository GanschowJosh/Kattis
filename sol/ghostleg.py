n,m=map(int, input().split())

curr = list(range(1,n+1))
for _ in range(m):
  a=int(input())
  curr[a-1],curr[a]=curr[a],curr[a-1]

for i in curr:
  print(i)