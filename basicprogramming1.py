def median(a, b, c):
  return max(min(a, b), min(max(a, b), c))

n, t = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
sum_even = sum(x for x in a if x % 2 == 0)
seq = [chr((x % 26) + 97) for x in a]

if t == 1:
  print("7")
elif t == 2:
  print("Bigger" if a[0] > a[1] else "Equal" if a[0] == a[1] else "Smaller")
elif t == 3:
  print(median(a[0], a[1], a[2]))
elif t == 4:
  print(sum_a)
elif t == 5:
  print(sum_even)
elif t == 6:
  print(''.join(seq))
elif t == 7:
  numcomps = 0
  ind = 0
  while True:
    if ind > n - 1:
      print("Out")
      break
    ind = a[ind]
    numcomps += 1
    if ind == n - 1:
      print("Done")
      break
    if numcomps > n:
      print("Cyclic")
      break