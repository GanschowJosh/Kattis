from collections import defaultdict
n,k,c=map(int, input().split())

teams = []
for _ in range(n):
  teams.append(list(map(int, input().split())))

out = 0
cou=defaultdict(int)
taken = [False]*n
for i,(t,s) in enumerate(teams):
  if out == k: break
  if cou[s] >= c: continue
  taken[i]=True
  cou[s]+=1
  out+=1


for i,(t,s) in enumerate(teams):
  if taken[i]: continue
  if out == k: break
  taken[i]=True
  out += 1

for i in range(n):
  if taken[i]:
    print(teams[i][0])
