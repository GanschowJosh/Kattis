t=int(input())
for _ in range(t):
  needed=[False]*4
  n=int(input())
  p=list(map(int, input().split()))

  for i in p:
    if all(needed): break
    if i >= 1 and i <= 10:
      needed[0]=True
    if i > 10 and i <= 20:
      needed[1]= True
    if i > 20 and i <= 30:
      needed[2]=True
    if i > 30 and i <= 40:
      needed[3]=True

  su=0
  for i in needed:
    if i: su+=1

  print(su)