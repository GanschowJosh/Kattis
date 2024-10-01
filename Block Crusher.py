from collections import deque
def minCost(grid):
    if not grid or not grid[0]:
        return 0, []
    
    rows, cols = len(grid), len(grid[0])

    dist = [[float('inf')] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    directions = [(-1, 0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    
    queue = deque()
    
    for j in range(cols):
        dist[0][j] = grid[0][j]
        queue.append((0,j))

    while queue:
        x, y = queue.popleft()
        
        #checking all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
        
            if 0 <=nx < rows and 0 <= ny < cols:
                newCost = dist[x][y] + grid[nx][ny]

                if newCost < dist[nx][ny]:
                    dist[nx][ny] = newCost
                    prev[nx][ny] = (x, y)
                    queue.append((nx, ny))
    
    min_cost = float('inf')
    endCol = -1
    for j in range(cols):
        if dist[-1][j] < min_cost:
            min_cost = dist[-1][j]
            endCol = j
    
    #backtrack to find the actual path
    path = []
    current = (rows-1, endCol)
    while current:
        path.append(current)
        current=prev[current[0]][current[1]]
    
    path.reverse()

    return min_cost, path

def printgrid(grid, path):
    path = set(path)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i,j) in path:
                print(' ', end='')
            else:
                print(cell, end='')
        print()
while True:

    grid = []
    h, w = list(map(int, input().split()))
    if h == 0 and w == 0:
        break
    for _ in range(h):
        grid.append(list(map(int, input())))
    min_cost, path = minCost(grid)
    printgrid(grid, path)
