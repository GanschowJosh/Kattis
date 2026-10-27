from collections import deque

n=int(input())
for _ in range(n):
  m=bytearray(input(), 'ascii')
  i=sum(2**(12-i-1) if m[i]==ord('o') else 0 for i in range(12))
  # print(bin(mask))
  if i.bit_count() < 2:
    print(i.bit_count())
    continue
  mn=10**10
  q=deque([i])
  vis=set()
  while q:
    cb=q.popleft()
    if cb in vis: continue
    vis.add(cb)
    cbc=cb.bit_count()
    # print(bin(cb))
    mn=min(mn,cbc)
    for j in range(10):
      if not(cb&(1<<(j+2))) and cb&(1<<(j+1)) and cb&(1<<j):
        nxt=cb
        nxt&=~(1<<j)
        nxt&=~(1<<(j+1))
        nxt|=(1<<(j+2))
        q.append(nxt)
      if not(cb&(1<<j)) and cb&(1<<(j+1)) and cb&(1<<(j+2)):
        nxt=cb
        nxt|=(1<<j)
        nxt&=~(1<<(j+1))
        nxt&=~(1<<(j+2))
        q.append(nxt)
  print(mn)
