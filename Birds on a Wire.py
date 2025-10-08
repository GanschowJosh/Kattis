l, d, n = list(map(int, input().split()))
positions = [int(input()) for _ in range(n)]

if positions:
  positions.sort()
  addlbirds = 0
  """FORMULA to find how many birds can fit in a given range min-max and a min distance between them d:
  max-min//d
  """
  #space before first bird
  if positions[0] > 6:
    addlbirds += (positions[0] - 6) // d

  #spaces between birds
  for i in range(1, n):
    space = positions[i]-positions[i-1]
    if space > d:
      addlbirds += (space - d) // d

  #space after last bird
  if l - positions[-1] > 6:
    addlbirds += (l-positions[-1] - 6) // d

else:
  addlbirds = (l-12)//d+1
print(addlbirds)