a=bytearray(input(), 'ascii')
b=bytearray(input(), 'ascii')

pref=0
cntp=0
for i in range(min(len(b), len(a))):
  if b[i]!=a[i]:break
  if b[i]==ord('1'): cntp+=1
  pref+=1

if len(b) > len(a):
  print(len(b))
else:
  # cnt=0
  # bb=b[:]
  # bb=b[:pref]
  # bb.extend(bytearray('1'*(len(b)-pref), 'ascii'))
  print(cntp+len(b)-pref)
  # print(bb)