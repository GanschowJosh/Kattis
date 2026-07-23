from collections import deque, defaultdict, Counter

n,m,d=map(int, input().split())
mine=list(map(int, input().split()))
opps=list(map(int, input().split()))

if d >= sum(mine)+sum(opps):
  print(1)
  exit()

start=(tuple(sorted(mine)), tuple(sorted(opps)), d)

q=deque([start])
prob=defaultdict(float)
prob[start]=1.0
seen={start}

answer=0.0

while q:
  mi,op,cd=q.popleft()
  p=prob[(mi,op,cd)]

  if all(o==0 for o in op):
    answer+=p
    continue

  if cd==0:
    continue

  alive=sum(x>0 for x in mi)+sum(x>0 for x in op)
  transition_prob=p/alive

  mi=list(mi)
  op=list(op)

  counts=Counter(mi)

  for health, count in counts.items():
    nmi=list(mi)
    nmi.remove(health)

    if health>1: nmi.append(health-1)

    state=(tuple(sorted(nmi)), tuple(op), cd-1)
    prob[state]+=p*count/alive

    if state not in seen:
      seen.add(state)
      q.append(state)

  counts=Counter(op)
  for health, count in counts.items():
      nop=list(op)
      nop.remove(health)
  
      if health>1: nop.append(health-1)
  
      state=(tuple(mi), tuple(sorted(nop)), cd-1)
      prob[state]+=p*count/alive
  
      if state not in seen:
        seen.add(state)
        q.append(state)

print(answer)