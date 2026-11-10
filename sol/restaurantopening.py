n,m=map(int, input().split())
gr=[]
for _ in range(n):
  gr.append(list(map(int, input().split())))

mn=10**10
for i in range(n):
  for j in range(m):
    curr=0
    for k in range(n):
      for l in range(m):
        if i==k and j == l: continue
        curr+=((abs(i-k)+abs(j-l))*gr[k][l])
    mn=min(mn,curr)
print(mn)