from math import sqrt

def distance(p1, p2):
  return sqrt((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)

def linearInterp(t, t1, p1, t2, p2):
  ratio = (t-t1) / (t2-t1)
  x = p1[0] + ratio * (p2[0]-p1[0])
  y = p1[1] + ratio * (p2[1]-p1[1])
  return (x, y)

n, t = list(map(int, input().split()))
actualPath = []
totalTime = 0

for _ in range(n):
  x, y, time = list(map(int, input().split()))
  actualPath.append((time,(x,y)))
  totalTime = max(totalTime, time)

gpsPath = [actualPath[0]]
for i in range(t, totalTime, t):
  for j in range(len(actualPath)-1):
    t1, p1 = actualPath[j]
    t2, p2 = actualPath[j+1]
    if t1 <= i < t2:
      gpsPath.append((i, linearInterp(i, t1, p1, t2, p2)))
      break

gpsPath.append(actualPath[-1])

actualDist = sum(distance(p1[1], p2[1]) for p1, p2 in zip(actualPath, actualPath[1:]))
gpsDist = sum(distance(p1[1], p2[1]) for p1, p2 in zip(gpsPath, gpsPath[1:]))

errorPercentage = (actualDist - gpsDist) / actualDist * 100
print(gpsPath)
print(errorPercentage)