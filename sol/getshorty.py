while True:
  n,m=map(int, input().split())
  if n == 0 and m == 0: break
  gr=[[] for _ in range(n)]
  for _ in range(m):
    x,y,f=map(float, input().split())
    x=int(x)
    y=int(y)
    gr[x].append((y,f))
    gr[y].append((x,f))
  # print(gr)

  from collections import deque
  bst=[-1 for _ in range(n)]
  q=deque([(0,1)])
  while q:
    ci,cs=q.popleft()
    # print(ci,cs)
    if bst[ci] > cs: continue
    bst[ci]=cs
    for ni,f in gr[ci]:
      # print(ci, ni, f)
      if cs*f <= bst[ni]: continue
      bst[ni]=cs*f
      q.append((ni,cs*f))
  bf=bst[n-1]
  print(f"{bf:.4f}")