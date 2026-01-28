from collections import deque

N, M, S = map(int, input().split())
grid = []
for _ in range(N):
  grid.append(list(map(int, input().split())))

start = grid[0][0]
if start > S:
  print(-1)
  exit()

frontier = {(0,0): start}
steps = 0
goal = (N-1, M-1)

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while frontier:
  if goal in frontier and frontier[goal] <= S:
    print(steps)
    exit()
  
  next_frontier = {}
  for (r,c),cost in frontier.items():
    for dr, dc in dirs:
      nr, nc = r+dr, c+dc
      if 0 <= nr < N and 0 <= nc < M:
        ncst = cost + grid[nr][nc]
        if ncst <= S:
          prev = next_frontier.get((nr, nc))
          if prev is None or ncst < prev:
            next_frontier[(nr, nc)] = ncst
  frontier = next_frontier
  steps += 1

print(-1)
