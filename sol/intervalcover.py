while True:
  try: 
    a,b=map(float, input().split())
    n=int(input())
    inv=[]
    idx={}
    for i in range(n):
      x,y=map(float, input().split())
      inv.append((x,y))
      idx[(x,y)]=i
    inv.sort()
    i=ans=0
    ot=[]
    imp=False
    if a == b:
      for x,y in inv:
        if x <= a <= y:
          ot=[idx[(x,y)]]
          break
      else:
        imp=True
    while a < b:
      fart=a
      chosen=None
      while i < len(inv) and inv[i][0] <= a:
        if inv[i][1] > fart:
          fart=inv[i][1]
          chosen=idx[inv[i]]
        i+=1
      if chosen is None:
        imp=True
        break
      a=fart
      ot.append(chosen)
    if imp:
      print('impossible')
    else: 
      print(len(ot))
      print(' '.join(map(str, ot)))
  except EOFError:
    break