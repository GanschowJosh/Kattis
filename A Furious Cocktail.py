n, T = map(int, input().split())

t = []
for _ in range(n):
  t.append(int(input()))

t.sort(reverse=True)
ok = all(t[i] > (n - 1 - i) * T for i in range(n))
print("YES" if ok else "NO")