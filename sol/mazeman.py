from collections import deque
n,m=map(int, input().split())
gr = []
for _ in range(n):
  gr.append(bytearray(input(),'ascii'))

locs = dict()
entr = bytearray("ABCDEFGHIJKLMNOPQRSTUVW",'ascii')
entrances = []

reached = [bytearray(m) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if gr[i][j] in entr:
      locs[(i,j)]=False
      entrances.append((i,j))

needed = 0
move_to = entr+bytearray('. ', 'ascii')
for si,sj in entrances:
  if reached[si][sj]: continue
  q=deque([(si,sj)])
  found = False
  while q:
    ci,cj=q.popleft()
    curr=gr[ci][cj]
    for (di,dj) in [(-1,0),(0,-1),(0,1),(1,0)]:
      ni,nj=di+ci,dj+cj
      if 0 > ni or ni >= n or 0 > nj or nj >= m: continue
      if gr[ni][nj] in entr and curr in entr: continue
      if reached[ni][nj]: continue
      if gr[ni][nj] in move_to:
        q.append((ni,nj))
        reached[ni][nj] = 1
      if gr[ni][nj] == ord('.'):
        found = True
  if found:
    needed += 1


bad=0
for i in range(n):
  for j in range(m):
    if gr[i][j] == ord('.') and not reached[i][j]:
      bad+=1

print(needed, bad)