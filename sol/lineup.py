n=int(input())
inc,dec=True,False
last=None
for _ in range(n):
  curr=input()
  if last is None:
    last=curr
    continue
  # print(curr,last,curr<last)
  if curr > last and inc:
    last=curr
    continue
  if curr < last and dec: 
    last=curr
    continue
  if curr < last and _ <= 1:
    dec=True
    inc=False
    last=curr
    continue
  last=curr
  inc=False
  dec=False

if inc:
  print("INCREASING")
elif dec:
  print("DECREASING")
else:
  print("NEITHER")
