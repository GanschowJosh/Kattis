while True:
  try:
    n,m=map(int, input().split())
  except:
    break
  
  adj=[0]*n

  for _ in range(m):
    a,b=map(int, input().split())
    adj[a]|=(1<<b)
    adj[b]|=(1<<a)

  dp=[[False]*n for _ in range(1<<n)]
  dp[1][0]=True

  ans=1
  for mask in range(1<<n):
    for u in range(n):
      if not dp[mask][u]:
        continue

      if adj[u]&1: ans=max(ans,mask.bit_count())

      available=adj[u]&~mask
      while available:
        bit=available&-available
        v=bit.bit_length()-1
        dp[mask|bit][v]=True
        available-=bit
  print(ans)