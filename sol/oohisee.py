r,c=map(int, input().split())
gr=[]
for _ in range(r):
  gr.append(bytearray(input().strip(), 'ascii'))

fd=set()
for i in range(1, r-1):
  for j in range(1, c-1):
    if all(gr[i+di][j+dj]==ord('O') for di, dj in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]) and gr[i][j]==ord('0'):
      fd.add((i,j))

if len(fd)==0:
  print('Oh no!')
elif len(fd)==1:
  print(*map(lambda x: x+1, fd.pop()))
else:
  print(f'Oh no! {len(fd)} locations')
