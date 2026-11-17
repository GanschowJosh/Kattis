from fractions import Fraction
n=int(input())
block=1
curr=1
while curr + block <= n:
  curr+=block
  block+=1
left=n-curr
f=Fraction(left,block)
if left != 0:
  print(f"{block} {f.numerator}/{f.denominator}")
else:
  print(block)