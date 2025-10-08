n, s = map(int, input().split())
for _ in range(n):
  l, r = map(int, input().split())
  if l <= s and s <= r:
    s += 1
print(s)