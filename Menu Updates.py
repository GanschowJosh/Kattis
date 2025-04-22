""" NAIVE 
def next_available(days, U):
  for i in range(U):
    if days[i] == 0: #available state
      return i
  return -1

def update_days(days, U):
  for i in range(U):
    if days[i] not in [0, -1]:  #option currently in use or available
      days[i] -= 1

d, U = map(int, input().split())

days = [0]*U

for _ in range(U):
  curr = input().split()
  if curr[0] == "a":
    next = next_available(days, U)
    days[next] = -1 #taken state
    print(next+1)
  else:
    __, ret = curr
    days[int(ret)-1] = d
  update_days(days, U)
"""

import sys, heapq

d, U = map(int, sys.stdin.readline().split())

free = [0] #indices that are free
heapq.heapify(free)

cooling = [] #numbers that are cooling down

next_new = 1 #smallest int we've never used

on_menu = [False]*(U+5) #which nums are on menu

out = []
day = 0

for line in sys.stdin:
  while cooling and cooling[0][0] <= day:
    _, idx = heapq.heappop(cooling)
    heapq.heappush(free, idx)

  cmd = line[0]

  if cmd[0] == 'a':
    if free and free[0] < next_new:
      idx = heapq.heappop(free)
    else:
      idx = next_new
      next_new += 1

    on_menu[idx] = True
    out.append(str(idx+1))
  else:
    _, x = line.split()
    idx = int(x) - 1
    if on_menu[idx]:
      on_menu[idx] = False
      heapq.heappush(cooling, (day+d, idx))

  day += 1

sys.stdout.write('\n'.join(out))
