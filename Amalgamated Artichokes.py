p,a,b,c,d,n = map(int, input().split())

from math import sin, cos
def f(k):
  return p*(sin(a*k+b)+cos(c*k+d)+2)

prices = [f(k) for k in range(1, n+1)]

mxs = [0]*n
mxs[0] = prices[0]
mns = [float('inf')]*n
mns[-1] = prices[-1]

for i in range(1,n):
  mxs[i] = max(mxs[i-1], prices[i])

for i in range(n-2, -1, -1):
  mns[i] = min(mns[i+1], prices[i])

best = 0
for i in range(n-1):
  best = max(best, mxs[i] - mns[i+1])
print(best)
# print(mxs)
# print(mns)