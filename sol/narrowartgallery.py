from collections import deque, defaultdict
while True:
  n,k=map(int, input().split())
  if (n,k)==(0,0): exit()
  gal=[]
  for _ in range(n):
    gal.append(tuple(map(int, input().split())))
  bst={(0,0,0):0} #row,closed,lc: most we've gathered at that row
  q=deque([(0,0,0,0)])#current row, num closed, value lost, row closed (-1: left, 0: none, 1: right)
  while q:
    cr,cc,cv,lc=q.popleft()
    if cv > bst[(cr,cc,lc)]: continue
    # print(bst)
    for opt in [-1,0,1]:
      if opt == -1 and lc == 1: continue
      if opt == 1 and lc == -1: continue
      nv=cv
      if opt==-1:
        nv=gal[cr][0]+cv
      if opt == 1:
        nv=gal[cr][1]+cv
      nr=cr+1
      nc=cc+1 if opt else cc
      if nc > k: continue
      nxt=(nr,nc,nv,opt)
      # print(nxt)
      if (nr,nc,opt) in bst and bst[(nr,nc,opt)] <= nv: continue
      bst[(nr,nc,opt)]=nv
      if cr < n-1: q.append(nxt)
  su=0
  for row in gal:
    su+=sum(row)
  print(su-min(bst.get((n,k,i),float('inf')) for i in [-1,0,1]))
  