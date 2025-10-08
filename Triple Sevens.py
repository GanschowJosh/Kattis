n = int(input())
a = True
for _ in range(3):
  l = list(map(int, input().split()))
  if 7 not in l:
    a = False

print(777 if a else 0)