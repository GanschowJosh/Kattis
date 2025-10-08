t = int(input())
for i in range(t):
  currList = []
  n = int(input())
  for j in range(n):
    currList.append(str(input()))
  print(len(set(currList)))