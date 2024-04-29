from collections import deque

# Read the initial parameters
m, n, s0 = map(int, input().split())

# Read the transformation pairs
transformations = []
for _ in range(n):
    a, b = map(int, input().split())
    transformations.append((a, b))

# Initialize the queue and the visited set
queue = deque([(s0, 0)])
visited = set()

# Process states in the queue
while queue:
    current_state, distance = queue.popleft()

    # Skip if this state has been visited before
    if current_state in visited:
        continue

    # Mark this state as visited
    visited.add(current_state)

    # Check if we've reached the target state
    if current_state == 0:
        print(distance)
        exit(0)

    # Add all possible next states to the queue
    for a, b in transformations:
        next_state = (current_state * a + b) % m
        queue.append((next_state, distance + 1))

# If we've exhausted all states and haven't found a path to 0, print -1
print(-1)
