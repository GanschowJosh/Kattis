n=int(input())
mp={
  'S':0,
  'M':0,
  'L':0
}
most={
  'S':6,
  'M':8,
  'L':12
}
for _ in range(n):
  s,l=input().split()
  mp[s]+=int(l)
su=0
for sz, amt in mp.items():
  su+=amt//most[sz]
  if amt%most[sz]:
    su+=1
print(su)