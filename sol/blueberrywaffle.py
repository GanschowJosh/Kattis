r,f=map(int, input().split())
rot=f//r
left=f%r
if left > r // 2:
  rot += 1
print('down' if rot%2 else 'up')