import fractions
s = input()
l = list(map(int, list(s)))
n=len(s)

tot=n*(n+1)//2
curr=9*tot
for i in range(1,10):
  r=0
  for j,c in enumerate(l):
    if c >= i:
      curr-=(r*(r+1)//2)
      r=0
    else:
      r+=1
  curr-=r*(r+1)//2

# print(tot,curr)
p=curr//tot
pp=curr%tot
o=fractions.Fraction(pp,tot)
if o != 0:
  if p!=0:
    print(p, o)
  else:
    print(o)
else:
  print(p)