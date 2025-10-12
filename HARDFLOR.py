n = int(input())

ds = input().split()

curr = (0,0)
coords = list()
coords.append(curr)
for d in ds:
  a, b = d[0], int(d[1:])
  if a == 'N':
    curr = (curr[0], curr[1]+b)
  if a == 'E':
    curr = (curr[0]+b, curr[1])
  if a == 'S':
    curr = (curr[0], curr[1]-b)
  if a == 'W':
    curr = (curr[0]-b, curr[1])
  coords.append(curr)

def area(coords): #shoelace formula (works for any polygon)
  a = 0.5*abs(sum(coords[i][0]*coords[i+1][1]-coords[i+1][0]*coords[i][1] for i in range(1, n)))
  a += 0.5*abs((coords[n-1][0]*coords[0][1]-coords[0][0]*coords[n-1][1]))
  return a

print(f"THE AREA IS",int(area(coords)))