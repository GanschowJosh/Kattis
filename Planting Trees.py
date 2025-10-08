def earliest_party_day(n, growth_times):
  # Sort growth times in descending order
  growth_times.sort(reverse=True)
  
  # Track the latest maturity day
  latest_maturity_day = 0

  for day, growth_time in enumerate(growth_times, start=1):
    # Calculate the day each tree will mature
    maturity_day = day + growth_time
    latest_maturity_day = max(latest_maturity_day, maturity_day)

  # The earliest party day is the day after the last tree matures
  return latest_maturity_day + 1

n = int(input())
growth_times = list(map(int, input().split()))
print(earliest_party_day(n, growth_times))