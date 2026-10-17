while True:
  n=int(input())
  if n == 0: break
  names=[]
  for _ in range(n):
    names.append(input())
  srt=sorted(names, key=lambda x: x[:2])
  print('\n'.join(srt))
  print()
