n, q = map(int, input().split())
locs = list(map(int, input().split()))

for _ in range(q):
    op, a, b = map(int, input().split())
    if op == 1:
        locs[a-1] = b
    elif op == 2:
        print(max(locs[a-1]-locs[b-1], locs[b-1] - locs[a-1]))