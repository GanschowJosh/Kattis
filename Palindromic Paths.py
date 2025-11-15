r, c = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(list(input()))

p = int(input())
pals = []
for _ in range(p):
    pals.append(input())

neighbors = [
    [-1,-1],[-1,0],[-1,1],
    [0,-1],[0,1],
    [1,-1],[1,0],[1,1]
]

def search(x, y, pal, curr_idx, seen):
    if x < 0 or x >=r or y < 0 or y >= c: return False
    if (x, y) in seen: return False
    if grid[x][y] != pal[curr_idx]: return False
    if curr_idx == len(pal)-1: return True

    seen.add((x, y))
    for dx, dy in neighbors:
        if search(x+dx, y+dy, pal, curr_idx+1, seen):
            seen.remove((x, y))
            return True
    seen.remove((x, y))
    return False

for curr, pal in enumerate(pals):
    char = pal[0]
    out = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] == char:
                out |= search(i, j, pal, 0, set())
    print(f"Case {curr+1}: {'Yes' if out else 'No'}    {pal}")