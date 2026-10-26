from collections import deque, defaultdict
t=int(input()) 
for _ in range(t):
  m=int(input())
  heights=list(map(int, input().split()))
  q=deque([(heights[0],1,'U',heights[0])]) #curr height, num done, last move, max height
  best=defaultdict(lambda: 10**10)
  parent={}
  while q:
    ch,cp,lm,mx=q.popleft()
    if best[(cp,ch)] <= mx: continue
    best[(cp,ch)]=mx
    parent[(cp,ch)]=lm
    if cp == len(heights): continue
    nxt=heights[cp]
    if ch - nxt >= 0:
      q.append((ch-nxt,cp+1,'D',mx))
    q.append((ch+nxt,cp+1,'U',max(mx,ch+nxt)))
  # print(best[len(heights)])
  if best[(len(heights),0)] == 10**10:
    print('IMPOSSIBLE')
    continue
  ch=0
  ot=[]
  for curr in range(len(heights),0,-1):
    lm=parent[(curr,ch)]
    ot.append(lm)
    if lm=='D':
      ch += heights[curr-1]
    else:
      ch -= heights[curr-1]
  print(''.join(reversed(ot)))
  # mxo=10**10
  # bst=None
  # for mask in range(1<<len(heights)):
  #   curr=0
  #   mx=0
  #   o=[]
  #   for i in range(len(heights)):
  #     if mask & (1<<i): 
  #       o.append('U')
  #       curr+=heights[i]
  #     else: 
  #       o.append('D')
  #       curr-=heights[i]
  #     if curr < 0: break
  #     mx=max(mx, curr)
  #   if curr != 0: continue
  #   if mx < mxo:
  #     mxo=mx
  #     bst=o
  # if bst is None:
  #   print('IMPOSSIBLE')
  # else:
  #   print(''.join(bst))
