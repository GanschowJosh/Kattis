s=int(input())
states=[tuple(map(int, input().split())) for _ in range(s)]


costs=[]
tot=0
have=0
for i,state in enumerate(states):
  tot+=state[0]
  maj=(state[1]+state[2]+state[3])//2+1
  towin = maj-state[1]
  if towin <= 0:
    have+=state[0]
    continue
  if towin > state[3] or state[2] >= (state[1]+state[2]+state[3])/2: #not enough undecided to win or f already won
    continue
  costs.append((towin, state[0]))

needed=tot//2
needed+=1

# print(costs, needed, have)

feas=[10**10]*(tot+1)
costs.sort()
feas[0]=0
for cost, gain in costs:
  for i in range(tot, gain-1,-1):
    if feas[i-gain] != 10**10: feas[i]=min(feas[i-gain]+cost,feas[i])

rem=max(0,needed-have)
ans=min(feas[rem:])
print(ans if ans != 10**10 else 'impossible')