def max_cash(N, T, people):
  people.sort(reverse=True, key=lambda x: x[0])

  occupied_minutes = [None] * T
  total_cash = 0

  for cash, time_limit in people:
    for minute in range(min(time_limit, T - 1), -1, -1):
      if occupied_minutes[minute] is None:
        occupied_minutes[minute] = cash
        total_cash += cash
        break

  return total_cash

n, t = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(n)]
print(max_cash(n, t, people))
