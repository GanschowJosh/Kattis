def perfectCheck(n):
  if n == 1: return "almost perfect"
  s = 1
  i = 2
  while(i * i <= n):
    if(n%i == 0 ):
      s+=i
      if(i != n / i):
        s += n / i
    i += 1
  if s == n:
    return "perfect"
  elif abs(s-n) <= 2:
    return "almost perfect"
  else:
    return "not perfect"

while True:
  try:
    curr = int(input())
    print(f"{curr} {perfectCheck(curr)}")
  except:
    break