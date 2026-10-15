from collections import defaultdict
t=int(input())
for _ in range(t):
  last = defaultdict(str)
  gen = defaultdict(int)
  n,q,g=map(int,input().split())
  for _ in range(q):
    # print(last)
    # print(gen)
    inp = input().split()
    # print(inp)
    if inp[0] == 'Q':
      print(gen[int(inp[1])])
    else:
      s,a = map(int, [inp[1],inp[2]])
      p=map(int, inp[3:])
      for pe in p:
        gen[last[pe]]-=1
        last[pe]=s
      gen[s]+=a
  
