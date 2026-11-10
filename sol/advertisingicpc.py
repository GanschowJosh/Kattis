n,m=map(int, input().split())
gr=[]
for _ in range(n):
  gr.append(bytearray(input().strip(), 'ascii'))

ct=0
for i,row in enumerate(gr):
  ct+=sum(1 for i in row if i==ord('?'))

opts=[(ord('?'),ord('I')),(ord('?'),ord('C')),(ord('?'),ord('P')),(ord('?'),ord('C'))]

for i in range(n-1):
  for j in range(m-1):
    c=(gr[i][j],gr[i][j+1],gr[i+1][j],gr[i+1][j+1])
    good=True
    for k in range(4):
      if c[k] not in opts[k]: good=False
    if good:
      ct-=sum(1 for l in range(4) if c[l]==ord('?'))
      break
  if good: break
else:
  print(0)
  exit()

print(pow(3,ct,998_244_353))