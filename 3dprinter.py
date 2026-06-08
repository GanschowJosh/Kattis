from collections import deque

def min_days(n):
  initial_state = (1, 0, 0)

  queue = deque([initial_state])

  visited = set()

  while queue:
    printers, statues, days = queue.popleft()

    if statues >= n:
      return days

    new_states = [(printers, statues + printers, days + 1), (printers * 2, statues, days + 1)]

    for new_state in new_states:
      if new_state not in visited:
        visited.add(new_state)
        queue.append(new_state)


print(min_days(int(input())))
