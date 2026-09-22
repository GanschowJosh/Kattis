l = int(input())
line=input()

stack = []

br_map = {
  ')': '(',
  ']': '[',
  '}': '{'
}

opening = "({["
for i,char in enumerate(line):
  if char == ' ': continue
  if char in opening:
    stack.append(char)
  else:
    if not stack or stack[-1] != br_map[char]:
      print(f'{char} {i}')
      exit()
    else:
      stack.pop()

print('ok so far')