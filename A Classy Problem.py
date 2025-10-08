from collections import defaultdict
from functools import cmp_to_key

#storing name and class value
m = defaultdict(int)
v = []

#sorts vector, primarily by value, secondarily by name
def sortVec(a, b):
  al = m[a]
  bl = m[b]
  if al != bl:
    return m[b] - m[a] #sort by class value (descending)
  else:
    return (a > b) - (a < b) #sort by name (ascending)


t = int(input())
for _ in range(t):
  v.clear()
  m.clear()
  n = int(input())

  #reading input
  for _ in range(n):
    inpString = input().split()
    name = inpString[0][:-1]
    classString = str(inpString[1])
    

    #class val calculation
    classVal = ''
    for token in classString.split('-'):
      if token == "upper":
        classVal += '3'
      elif token == "middle":
        classVal += '2'
      elif token == "lower":
        classVal += '1'
    
    classVal = classVal[::-1]
    classVal = classVal.ljust(10, '2')

    value = int(classVal)
    m[name] = value
    v.append(name)

  v.sort(key=cmp_to_key(sortVec))

  for name in v:
    print(name)
  print("="*30)