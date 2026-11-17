def P(r,g):
  return (2*r*g)/((r+g)*(r+g-1))
from math import isqrt
a,b=map(int, input().split())
for r in range(1,10**6+1):
  A=a
  B=a*(2*r-1)-2*b*r
  C=a*r*(r-1)
  D=B**2-4*A*C
  if D < 0: continue
  sq=isqrt(D)
  if sq*sq != D: continue
  for numerator in (-B-sq, -B+sq):
    if numerator % (2*A):
      continue
    g = numerator // (2*A)
    if g > 0:
      print(r, g)
      exit()
print('impossible')
