n,m=map(int, input().split())
gr=[]
for _ in range(n):
  gr.append(bytearray(input().strip(), 'ascii'))

ct=0
for i,row in enumerate(gr):
  ct+=sum(1 for i in row if i==ord('?'))

MOD=998244353

I=ord('I')
C=ord('C')
P=ord('P')
Q=ord('?')


opts=[(ord('?'),ord('I')),(ord('?'),ord('C')),(ord('?'),ord('P')),(ord('?'),ord('C'))]

dp={(0,"", False): 1} #mask, previous letter, pattern found
for pos in range(n*m):
  nxt={}
  r,c=pos//m,pos%m
  ch=gr[r][c]
  for (mask,lst,fd),count in dp.items():
    nmsk=mask
    if ch == Q: allowed=['I','C','P']
    else: allowed=[chr(ch)]
    for a in allowed:
      nxfd=fd
      if c > 0 and mask&(1<<c) and lst=='P' and a=='C':
        nxfd=True
      if c > 0 and lst=='I' and a=='C':
        nmsk|=(1<<c)
      else:
        nmsk&=~(1<<c)
      nxst=(nmsk,a,nxfd)
      if nxst in nxt:nxt[nxst]+=count
      else: nxt[nxst]=count
      nxt[nxst]%=MOD
  dp=nxt

print(sum(count for (_,_,fd),count in dp.items() if fd)%MOD)