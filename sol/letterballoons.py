alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

idx={a: i for i,a in enumerate(alphabet)}

p,t=map(int, input().split())
nm=[]
for _ in range(t):
  nm.append(input().strip())

mx=0
for m in range(1<<t):
  taken=[False]*p
  bad=False
  for i in range(t):
    if m&(1<<i):
      for ch in nm[i]:
        if idx[ch] >= p:
          bad=True
          break
        # print(ch,idx[ch])
        if taken[idx[ch]]: 
          bad=True
          break
        taken[idx[ch]]=True
    if bad: break
  if not bad:
    mx=max(mx, m.bit_count())
print(mx)