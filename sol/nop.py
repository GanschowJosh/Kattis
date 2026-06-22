inp=input()
i=0
nops=0
for char in inp:
  if char.upper()==char:
    if i%4!=0:
      jmp=(4-(i%4))
      nops+=jmp
      i+=jmp
  i+=1
print(nops)