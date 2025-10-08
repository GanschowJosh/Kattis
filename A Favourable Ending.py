from collections import defaultdict
from functools import lru_cache

t = int(input())


for _ in range(t):
ending_map = defaultdict(str)
connection_map = defaultdict(list)
s = int(input())
for __ in range(s):
  line = input().split()
  ending = False
  try:
  line[1] = int(line[1])
  except:
  ending = True
  if not ending:
  curr, a, b, c = map(int, line)
  connection_map[curr].extend([a, b, c])
  else:
  curr, ending = line
  curr = int(curr)
  ending_map[curr] = ending

@lru_cache(maxsize=None)
def dfs(curr):
  if ending_map[curr] == "favourably":
  return 1
  return sum(dfs(neighbor) for neighbor in connection_map[curr])

print(dfs(1))