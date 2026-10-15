n,s,k=map(int, input().split())

locs = []
for _ in range(n):
  locs.append(int(input()))

locs.sort()

tot = 0
l=-1*10**9-locs[0]
for i, loc in enumerate(locs):
  if i == len(locs)-1:
    r = 10**9+(s/2)+loc
  else:
    r = locs[i+1]
  dist = min([loc-l, r-loc-s/2, k/2])
  if dist < s/2:
    print(-1)
    exit()
  tot += dist
  l = loc+dist

print(int(tot*2))