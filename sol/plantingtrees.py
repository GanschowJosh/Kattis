n = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

latest_maturity = 0

for day, tree_growth_time in enumerate(trees, 1):
  maturity_day = day + tree_growth_time
  #latest_maturity = max(latest_maturity, maturity_day)
  if maturity_day > latest_maturity:
    latest_maturity = maturity_day

print(latest_maturity + 1)