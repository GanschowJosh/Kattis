n,q=map(int, input().split())
s={}
pt=0
for _ in range(n):
  a=input()
  s[a]=pt
  pt+=1

for _ in range(q):
  a,b=input().split()
  print(max(s[a],s[b])-min(s[a],s[b])-1)

