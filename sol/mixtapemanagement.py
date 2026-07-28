n=int(input())
p=list(map(int, input().split()))

width=len(str(n))
o=[]

for i, rank in enumerate(p, start=1):
  o.append("1" + str(i).zfill(width) + "0" * rank)

print(*o)