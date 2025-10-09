
# while True:
#   try:
#     inp = int(input())
#     limit = 1
#     stan_turn = True
#     while limit < inp:
#       if stan_turn:
#         limit *= 9
#       else:
#         limit *= 2
#       stan_turn = not stan_turn
#     print("Ollie wins." if stan_turn else "Stan wins.")
#   except:
#     break

from functools import lru_cache

def mex(iter):
  g= 0
  s = set(iter)
  while g in s:
    g += 1
  return g

def solve(n):
  @lru_cache(maxsize=None)
  def grundy(v):
    if v >= n:
      return 0
    nxt = []
    for m in range(2, 10):
      u = v*m
      nxt.append(0 if u >= n else grundy(u))
    return mex(nxt)
  return grundy(1)

while True:
  try:
    n = int(input())
    print("Stan wins." if solve(n) else "Ollie wins.")
  except:
    break