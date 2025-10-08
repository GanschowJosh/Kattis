s = input().strip()
n = len(s)

counts = {'A': 0, 'B': 0, 'C': 0}
current = {'A': 0, 'B': 0, 'C': 0}
result = 0

for char in s:
  counts[char] -= 1
  current[char] += 1

  while all(current[c] > 0 for c in 'ABC'):
    for c in 'ABC':
      current[c] -= 1
    result += 1
  
  if any(counts[c] < result for c in 'ABC'):
    break

print(result)