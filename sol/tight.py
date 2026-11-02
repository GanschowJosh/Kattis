while True:
  try:
    k,n=map(int, input().split())
    if k in [0,1]:
      print(100)
      continue
    ct=[[0 for _ in range(k+1)] for __ in range(n+1)]
    ct[0]=[0]*(k+1)
    ct[1]=[1]*(k+1)
    for i in range(2,n+1):
      # print(ct)
      last=ct[i-1]
      curr=[0]*(k+1)
      curr[0]=last[1]+last[0]
      curr[k]=last[k-1]+last[k]
      for j in range(1,k):
        curr[j]=last[j-1]+last[j]+last[j+1]
      ct[i]=curr
    print(sum(ct[n])/((k+1)**n)*100)
  except EOFError: break