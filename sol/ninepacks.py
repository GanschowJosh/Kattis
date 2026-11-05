hot=list(map(int, input().split()[1:]))
bun=list(map(int, input().split()[1:]))


hot.sort()
suhot=sum(hot)
bun.sort()
subun=sum(bun)
# print(hot, bun)

hotfeas=[10**10]*(suhot+1)
hotfeas[0]=0
for pack in hot:
  for i in range(suhot, pack-1, -1):
    if hotfeas[i-pack] != 10**10: hotfeas[i]=min(hotfeas[i-pack]+1,hotfeas[i])

bunfeas=[10**10]*(subun+1)
bunfeas[0]=0
for pack in bun:
  for i in range(subun, pack-1, -1):
    if bunfeas[i-pack]!=10**10: bunfeas[i]=min(bunfeas[i-pack]+1,bunfeas[i])

# print(bunfeas, hotfeas)
mn=10**10
for i in range(1,min(subun,suhot)+1):
  if hotfeas[i]==10**10 or bunfeas[i]==10**10: continue
  # print(i, hotfeas[i],bunfeas[i])
  mn=min(mn, hotfeas[i]+bunfeas[i])
print(mn if mn != 10**10 else 'impossible')