import re
from collections import Counter

alphabet="abcdefghijklmnopqrstuvwxyz"

n=int(input())
words=[]
for _ in range(n):
  words.append(input().strip())

curr=[set(alphabet) for _ in range(5)]
req=Counter()

def parse(ret, guess):
  global curr
  all=True
  need=Counter()
  for i in range(5):
    if ret[i]=='O':
      curr[i]=[guess[i]]
      need[guess[i]]+=1
    if ret[i]=='X':
      all=False
      if guess[i] in curr[i]: curr[i].discard(guess[i])
    if ret[i]=='/':
      all=False
      if guess[i] in curr[i]: curr[i].discard(guess[i])
      need[guess[i]]+=1
  for ch,c in need.items():
    req[ch]=max(req[ch],c)
  if all:
    exit()

def cf():
  global words
  global curr
  rstr=''
  for ch,c in req.items():
    rstr+=f'(?=(?:.*{ch}){{{c}}})'
  rstr+='('
  for item in curr:
    rstr+=('['+''.join(item)+']')
  rstr+=')'
  #print(rstr)
  pat=re.compile(rstr)
  words=[word for word in words if pat.fullmatch(word)]
  if words:
    return words[0]
  return None

while True:
  cg=cf()
  if cg is None: break
  print(cg, flush=True)
  parse(input().strip(), cg)
  