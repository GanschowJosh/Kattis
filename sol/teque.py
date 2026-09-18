import sys
from collections import deque
input=sys.stdin.readline
out=sys.stdout.write

N=int(input().strip())

left, right = deque(), deque()

for _ in range(N):
  op, it = input().strip().split()
  it=int(it)
  if op == 'push_back':
    right.append(it)
    while len(left) not in (len(right), len(right)+1):
      left.append(right.popleft())
  if op == 'push_front':
    left.appendleft(it)
    while len(left) not in (len(right), len(right)+1):
      right.appendleft(left.pop())
  if op == 'push_middle':
    left.append(it)
    while len(left) not in (len(right), len(right)+1):
      right.appendleft(left.pop())
  if op == 'get':
    if it < len(left):
      out(f'{left[it]}\n')
    else:
      out(f'{right[it-len(left)]}\n')