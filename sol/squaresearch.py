n = int(input())
grid = [input() for _ in range(n)]

dp = [[0] * n for _ in range(n)]
best = 0
bestr=None
bestc=None

for i in range(n):
  for j in range(n):
    if grid[i][j] == "#":
      if i == 0 or j == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = 1 + min(
          dp[i - 1][j],
          dp[i][j - 1],
          dp[i - 1][j - 1],
        )
      if dp[i][j]>best:
        best=dp[i][j]
        bestr=i-best+1
        bestc=j-best+1

print(bestr, bestc, best)