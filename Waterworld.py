n, m = map(int, input().split())
matr = []
for _ in range(n):
  matr.append(list(map(int, input().split())))

s = 0
for i in range(n):
  for j in range(m):
    s += matr[i][j]

print(s / (m*n))