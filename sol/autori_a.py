line=input()
out=[]
last = None
for char in line:
  if not last or last == '-':
    out.append(char)
  last=char
print(''.join(out))