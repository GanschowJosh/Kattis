from collections import defaultdict

m, n = map(int, input().split())

d = defaultdict(int)

for _ in range(m):
  a,b = input().split()
  d[a] = int(b)

for _ in range(n):
  s = 0
  while True:
    currEntry = input()
    if currEntry=='.':
      break
    for word in currEntry.split():
      if word in d:
        s += d[word]
    # s = sum(d[word] for word in currEntry)
  print(s)