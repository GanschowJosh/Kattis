l=int(input())

line = input().strip()

stack = []

rights = {
  ')': '(',
  '}': '{',
  ']': '['
}

for i,ch in enumerate(line):
  if ch == ' ': continue
  if ch in rights:
    if not stack or stack[-1] != rights[ch]: 
      print(ch, i)
      exit()
    else:
      stack.pop()
  else:
    stack.append(ch)
print("ok so far")