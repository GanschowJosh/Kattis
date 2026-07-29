from collections import defaultdict
n=int(input())

for _ in range(n):
  name=input()
  inp=input().split()
  num=int(inp[0])
  curr = []
  while len(curr) < num:
    line=list(input().split())
    if len(line) > 1:
      curr.extend(map(str, range(int(line[1]), int(line[2])+1, int(line[3]))))
    else:
      curr.extend(line)
  needed=defaultdict(int)
  for i in curr:
    for c in i:
      needed[c]+=1
  tot=0
  print(name)
  print(f"{num} address{'es' if num!=1 else ''}")
  for i in range(10):
    v=needed.get(str(i), 0)
    print(f"Make {v} digit {i}")
    tot+=v
  print(f"In total {tot} digit{'s' if tot != 1 else ''}")