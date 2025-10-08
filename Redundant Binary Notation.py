N, t = map(int, input().split())

# memoize
memo = {}

def calculate(N, d):
  # if depth is 0, check if N is 0
  if d == 0:
    return N == 0
  
  # optimizations - pruning
  if t * ((1 << d) - 1) < N:
    return 0
  
  # if the result for the current (N, d) is already computed, return it
  if (N, d) in memo:
    return memo[(N, d)]
  
  total = 0
  
  # recursively calculate the possibilities
  for i in range(t + 1):
    if (i << (d - 1)) <= N:
      total += calculate(N - (i << (d - 1)), d - 1)
  
  total %= 998244353
  
  memo[(N, d)] = total
  return total

# calculate and print the result
depth = len(bin(N)) - 2
print(calculate(N, depth))