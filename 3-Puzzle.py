from collections import deque

s = input().strip() + input().strip()

goal = "123-"
if s == goal:
    print(0)
    raise SystemExit

adj = {
    0: (1, 2),
    1: (0, 3),
    2: (0, 3),
    3: (1, 2),
}

def bfs(start, target):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        cur, d = q.popleft()
        if cur == target:
            return d
        z = cur.index('-')
        for nb in adj[z]:
            lst = list(cur)
            lst[z], lst[nb] = lst[nb], lst[z]
            nxt = ''.join(lst)
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, d + 1))
    return -1

print(bfs(s, goal))
