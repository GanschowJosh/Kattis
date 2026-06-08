import math

def min_sprinklers_to_cover(n, l, w, sprinklers):
  intervals = []
  half_width = w / 2.0
  for x, r in sprinklers:
    if r <= half_width:
      continue
    reach = math.sqrt(r**2 - half_width**2)
    left_end = x - reach
    right_end = x + reach
    intervals.append((left_end, right_end))
  
  intervals.sort()
  
  covered_end = 0
  count = 0
  i = 0
  while covered_end < l:
    farthest_reach = covered_end
    while i < len(intervals) and intervals[i][0] <= covered_end:
      farthest_reach = max(farthest_reach, intervals[i][1])
      i += 1

    if farthest_reach == covered_end:
      return -1

    covered_end = farthest_reach
    count += 1

    if covered_end >= l:
      break

  return count

try:
  while True:
    n, l, w = map(int, input().split())
    sprinklers = [tuple(map(int, input().split())) for _ in range(n)]
    print(min_sprinklers_to_cover(n, l, w, sprinklers))
except EOFError:
  pass
