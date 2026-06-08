def earliest_party_day(n, growth_times):
  growth_times.sort(reverse=True)
  
  latest_maturity_day = 0

  for day, growth_time in enumerate(growth_times, start=1):
    maturity_day = day + growth_time
    latest_maturity_day = max(latest_maturity_day, maturity_day)

  return latest_maturity_day + 1

n = int(input())
growth_times = list(map(int, input().split()))
print(earliest_party_day(n, growth_times))
