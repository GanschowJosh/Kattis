t=int(input())
for _ in range(t):
  m=int(input())
  n=int(input())
  opts=list(int(input()) for _ in range(n))

  mx=max(opts)
  seen=[float('inf')]*(m+mx+1)
  seen[0]=0
  for opt in opts:
    for s in range(m+mx, opt-1, -1):
      seen[s]=min(seen[s],seen[s-opt]+1)

  for i in range(m, m+mx+1):
    if seen[i]==float('inf'): continue
    print(f'{i} {seen[i]}')
    break
