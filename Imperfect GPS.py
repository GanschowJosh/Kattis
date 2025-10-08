from math import sqrt
def linearInterpolate(value, x1, y1, v1, x2, y2, v2):
  ratio = (value - v1) / (v2 - v1)

  xval = x1 + ratio * (x2-x1)
  yval = y1 + ratio * (y2-y1)

  return (xval, yval)

def distcalc(points):
  d = 0
  for i in range(len(points)-1):
    d += sqrt((points[i+1][0] - points[i][0])**2 + (points[i+1][1] - points[i][1])**2)
  return d

n, t = list(map(int, input().split()))
needed = [i for i in range(0, n*t, t)]
confirmedpts = []
trackedpts = []
totalDist = 0
trackedDist = 0
x, y, time = list(map(int, input().split()))
confirmedpts.append((x, y))
for _ in range(n-1):
  newx, newy, newtime = list(map(int, input().split()))
  need = [a for a in needed if time <= a <= newtime]
  for b in need: #looping through all the points that lie in between current time slot
    trackedpts.append(linearInterpolate(b, x, y, time, newx, newy, newtime))
  if _ == n-2:
    trackedpts.append((newx, newy))
  x, y, time = newx, newy, newtime
  confirmedpts.append((x, y))

true = distcalc(confirmedpts)
observed = distcalc(trackedpts)
print(abs(true-observed)/true * 100)