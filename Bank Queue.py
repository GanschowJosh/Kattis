def max_cash(N, T, people):
  # Sort people by cash in descending order
  people.sort(reverse=True, key=lambda x: x[0])

  # Track the slots with None (unoccupied) initially
  occupied_minutes = [None] * T
  total_cash = 0

  # Try placing each person in the latest available slot they can wait for
  for cash, time_limit in people:
    # Start from the latest minute they can wait and go backwards
    for minute in range(min(time_limit, T - 1), -1, -1):
      if occupied_minutes[minute] is None:  # If minute is unoccupied
        occupied_minutes[minute] = cash
        total_cash += cash
        break

  return total_cash

n, t = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(n)]
print(max_cash(n, t, people))