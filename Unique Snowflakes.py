from collections import deque

cases = int(input())

for _ in range(cases):
  n = int(input())
  q = deque()
  s = set()

  total = 0

  for _ in range(n):
    temp = int(input())
    if temp in s:
      while q[0] != temp:
        s.remove(q.popleft())
      q.popleft()
      q.append(temp)
    else:
      q.append(temp)
      s.add(temp)
      total = max(total, len(q))
    
  print(total)