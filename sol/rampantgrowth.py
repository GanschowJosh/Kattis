import sys
MOD = 998244353
r, c = map(int, input().split())
if c == 1:
  print(r % MOD)
  sys.exit()

dp = [[0] * r for _ in range(c)]

for row in range(r):
  dp[0][row] = 1

for col in range(1, c):
  for row in range(r):
    for prev_row in range(r):
      if prev_row != row:
        dp[col][row] = (dp[col][row] + dp[col - 1][prev_row]) % MOD

result = sum(dp[c - 1][row] for row in range(r)) % MOD
print(result)
