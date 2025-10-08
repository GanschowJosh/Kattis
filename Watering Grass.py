import math

def min_sprinklers_to_cover(n, l, w, sprinklers):
  # Compute the effective coverage of each sprinkler if it can reach width
  intervals = []
  half_width = w / 2.0
  for x, r in sprinklers:
    if r <= half_width:
      continue  # Skip sprinklers that don't cover the width
    reach = math.sqrt(r**2 - half_width**2)
    left_end = x - reach
    right_end = x + reach
    intervals.append((left_end, right_end))
  
  # Sort intervals by their starting point (left_end), and by right_end descending for tie-breaking
  intervals.sort()
  
  # Greedily cover the entire strip [0, l]
  covered_end = 0
  count = 0
  i = 0
  while covered_end < l:
    # Find the sprinkler that covers the farthest starting from covered_end
    farthest_reach = covered_end
    while i < len(intervals) and intervals[i][0] <= covered_end:
      farthest_reach = max(farthest_reach, intervals[i][1])
      i += 1

    # If we cannot extend the coverage further, return -1
    if farthest_reach == covered_end:
      return -1

    # Update covered end and increment sprinkler count
    covered_end = farthest_reach
    count += 1

    # If we have covered the entire length, break
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