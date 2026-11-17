g=input()
n=len(g)
def t(i):
  w,l=0,0
  a,b=0,0
  for j in range(n):
    if g[j]=='A':
      a+=1
    else:
      b+=1
    if a == i:
      w+=1
      a,b=0,0
    if b == i:
      l+=1
      a,b=0,0
  return w > l

fd=[]
for i in range(1,n+1):
  if t(i):
    fd.append(i)
print(len(fd))
if fd:
  print(*fd)