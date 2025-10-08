name = input()
newname = str()
lastchar = ''
for char in name:
  if char != lastchar:
    newname+=char
    lastchar = char
print(newname)