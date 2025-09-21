n, p = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

orders = set()

for j in range(p):
    col = [a[i][j] for i in range(n)]

    if len(set(col)) < n:
        continue

    order = tuple(sorted(range(n), key=lambda i: col[i]))
    orders.add(order)

print(len(orders))