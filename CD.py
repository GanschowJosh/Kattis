while True:
  n, m = map(int, input().split())
  
  if n == 0 and m == 0:
    break
  
  jack = set(int(input()) for _ in range(n))
  
  count = 0
  for _ in range(m):
    cd = int(input())
    if cd in jack:
      count += 1
  
  print(count)