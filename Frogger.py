"""from collections import deque

class FroggerReachabilityChecker:
  def __init__(self, grid):
    self.grid = [row[:] for row in grid]
    self.rows = len(grid)
    self.cols = len(grid[0])
    self.directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # Stay, Up, Down, Left, Right
    self.start = self.find_position('F')
    self.goal = self.find_position('G')
    self.car_rows = [i for i, row in enumerate(grid) if 'X' in row]
    self.precompute_car_positions()

  def find_position(self, char):
    return next((i, j) for i, row in enumerate(self.grid) 
          for j, cell in enumerate(row) if cell == char)

  def precompute_car_positions(self):
    self.car_positions = {}
    for i in self.car_rows:
      row = self.grid[i]
      car_indices = [j for j, cell in enumerate(row) if cell == 'X']
      self.car_positions[i] = car_indices

  def is_safe(self, x, y, time):
    if x in self.car_rows:
      car_positions = self.car_positions[x]
      if x % 2 == 0:  # Move right
        car_positions = [(pos - time) % self.cols for pos in car_positions]
      else:  # Move left
        car_positions = [(pos + time) % self.cols for pos in car_positions]
      return y not in car_positions
    return True

  def moves_to_reach_goal(self, max_moves):
    queue = deque([(self.start, 0)])  # (position, moves)
    visited = set()

    while queue:
      (x, y), moves = queue.popleft()

      if moves > max_moves:
        continue

      if (x, y) == self.goal:
        return moves

      state = (x, y, moves % self.cols)
      if state in visited:
        continue
      visited.add(state)

      for dx, dy in self.directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
          if self.is_safe(new_x, new_y, moves + 1):
            queue.append(((new_x, new_y), moves + 1))

    return -1  # Goal not reachable within max_moves

scenarios = int(input())
for _ in range(scenarios):
  x = int(input())
  n, m = list(map(int, input().split()))
  grid = []
  for i in range(n+2):
    grid.append(list(str(i) for i in input()))
  checker = FroggerReachabilityChecker(grid)
  turns = checker.moves_to_reach_goal(x)

  if turns != -1:
    print(f"The minimum number of turns is {turns}.")
  else:
    print("The problem has no solution.")"""
from collections import deque

class State:
  def __init__(self, x, y, distance):
    self.x = x
    self.y = y
    self.distance = distance

  def forward(self):
    return State(self.x, self.y + 1, self.distance + 1)

  def backward(self):
    return State(self.x, self.y - 1, self.distance + 1)

  def left(self):
    return State(self.x - 1, self.y, self.distance + 1)

  def right(self):
    return State(self.x + 1, self.y, self.distance + 1)

  def still(self):
    return State(self.x, self.y, self.distance + 1)


class Road(list):
  def __init__(self):
    super().__init__()
    self.q = deque()
    self.visited = [[[False for _ in range(51)] for _ in range(22)] for _ in range(51)]
    self.width = 0
    self.height = 0
    self.max_turns = 0

  def car_present(self, s):
    offset = self.width - (s.distance % self.width) if s.y % 2 == 1 else s.distance % self.width
    return self.lane(s.y)[(s.x + offset) % self.width] == 'X'

  def try_state(self, s):
    if (0 <= s.x < self.width and
        0 <= s.y <= self.height + 1 and
        s.distance <= self.max_turns and
        not self.visited[s.x][s.y][s.distance % self.width] and
        not self.car_present(s)):
      self.mark_visited(s)
      self.q.append(s)

  def get_min_turns(self):
    self.visited = [[[False for _ in range(51)] for _ in range(22)] for _ in range(51)]
    self.q.clear()

    goal_x = self.finish_x()
    self.q.append(State(self.start_x(), 0, 0))

    while self.q:
      s = self.q.popleft()

      if s.x == goal_x and s.y == self.height + 1:
        return s.distance

      self.try_state(s.left())
      self.try_state(s.right())
      self.try_state(s.forward())
      self.try_state(s.backward())
      self.try_state(s.still())

    return -1

  def lane(self, y):
    return self[self.height + 1 - y]

  def start_x(self):
    return self.lane(0).find("F")

  def finish_x(self):
    return self.lane(self.height + 1).find("G")

  def mark_visited(self, s):
    self.visited[s.x][s.y][s.distance % self.width] = True

n_cases = int(input())
for _ in range(n_cases):
  road = Road()
  road.max_turns = int(input())
  road.height, road.width = map(int, input().split())
  for _ in range(road.height + 2):
    road.append(input().strip())

  min_turns = road.get_min_turns()
  if min_turns >= 0:
    print(f"The minimum number of turns is {min_turns}.")
  else:
    print("The problem has no solution.")
