from collections import deque

def find_components(arr, r, c):
  comp = [[-1]*c for _ in range(r)]
  comp_id = 0
  dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  for i in range(r):
    row = arr[i]
    for j in range(c):
      if comp[i][j] != -1:
        continue
      comp[i][j] = comp_id
      digit = row[j]
      q = deque([(i, j)])
      while q:
        x, y = q.popleft()
        for dx, dy in dirs:
          nx, ny = x + dx, y + dy
          if 0 <= nx < r and 0 <= ny < c and comp[nx][ny] == -1 and arr[nx][ny] == digit:
            comp[nx][ny] = comp_id
            q.append((nx, ny))
      comp_id += 1
  return comp

r, c = map(int, input().split())

arr = []
for _ in range(r):
  arr.append(input())

n = int(input())

comp = find_components(arr, r, c)

for _ in range(n):
  x1, y1, x2, y2 = map(int, input().split())
  x1-=1
  x2-=1
  y1-=1
  y2-=1
  if comp[x1][y1] == comp[x2][y2]:
    if (arr[x1][y1] == '1'):
      print('decimal')
    else:
      print('binary')
  else:
    print('neither')