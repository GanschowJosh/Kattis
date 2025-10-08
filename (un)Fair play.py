blocks = []
while(True):
  line = input().strip()
  if line == "-1":
    break
  if line == "":
    continue
  n, m = list(map(int, line.split()))
  teampts = list(map(int, input().split()))
  winlist = []
  remainingmatches = []
  for i in range(m):
    team1, team2 = map(int, input().strip().split())
    remainingmatches.append((team1, team2))
  blocks.append((n, teampts, remainingmatches))

def calc(block):
  n, pts, matches = block
  winlist = [0 for _ in range(len(matches))]
  for match in matches:
    a, b = match
    if(a != n and b != n): #my team not playing
      if pts[a-1] == pts[b-1]: #tied pts
        pts[a-1] += 1
        pts[b-1] += 1
        winlist.append(1)
      elif pts[a-1] > pts[b-1]: #a much higher than b
        pts[b-1] += 2 #make b win
        winlist.append(2)
      elif pts[b-1] > pts[a-1]: #b much higher than a
        pts[a-1] += 2 #make a win
        winlist.append(0)
    else:
      pts[n-1] += 2
      if a==n:
        winlist.append(0)
      else:
        winlist.append(2)
  return (pts, winlist)

for block in blocks:
  p, w = calc(block)
  if(max(p[:-1]) >= p[-1]):
    print("NO")
  else:
    for i in w:
      print(i, end=" ")
    print()
    
    
    