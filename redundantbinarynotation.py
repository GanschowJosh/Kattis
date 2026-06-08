N, t = map(int, input().split())

memo = {}

def calculate(N, d):
  if d == 0:
    return N == 0
  
  if t * ((1 << d) - 1) < N:
    return 0
  
  if (N, d) in memo:
    return memo[(N, d)]
  
  total = 0
  
  for i in range(t + 1):
    if (i << (d - 1)) <= N:
      total += calculate(N - (i << (d - 1)), d - 1)
  
  total %= 998244353
  
  memo[(N, d)] = total
  return total

depth = len(bin(N)) - 2
print(calculate(N, depth))
