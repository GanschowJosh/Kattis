r,c,d=map(int, input().split())

gr=[]
for i in range(r):
  gr.append(list(map(int, input().split())))


import heapq

q=[(0,0,0)] #jumps, r, c

bst=[[10**10 for _ in range(c)] for _ in range(r)]
bst[0][0]=0
while q:
  cj,cr,cc=heapq.heappop(q)
  #print(cj,cr,cc)
  #print(q)
  if bst[cr][cc]<cj: continue
  for nr,nc in [[cr-1,cc],[cr,cc-1],[cr,cc+1],[cr+1,cc]]:
    if 0 > nr or nr >= r or 0 > nc or nc >= c: continue
    if gr[nr][nc]==0: continue
    if bst[nr][nc] <= cj: continue
    bst[nr][nc]=cj
    heapq.heappush(q,(cj,nr,nc))
  for i in range(d+2):
    for j in range(d+2):
      for nr,nc in [[cr-i,cc+j],[cr+j,cc-i],[cr+j,cc+i],[cr+i,cc+j],[cr-i,cc-j],[cr-j,cc-i],[cr-j,cc+i],[cr+i,cc-j]]:
        if 0 > nr or nr >= r or 0 > nc or nc >= c: continue
        if abs(i)+abs(j) > d+1: continue
        if gr[nr][nc]==0: continue
        if bst[nr][nc] <= cj+1: continue
        #print(nr,nc,cj+1)
        bst[nr][nc]=cj+1
        heapq.heappush(q,(cj+1,nr,nc))
print(bst[r-1][c-1] if bst[r-1][c-1] != 10**10 else -1)