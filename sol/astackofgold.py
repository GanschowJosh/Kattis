t=29260
g=29370

w,s=map(int, input().split())
pref=[0]
for i in range(1,s+1):
  pref.append(pref[-1]+(t*(i-1)))
post=[0]*(s+1)
for i in range(s-1, 0, -1):
  post[i]=post[i+1]+(t*(i+1))

print(pref, post)

for i in range(1,s+1):
  if pref[i]+post[i]+g*i == w:
    print(i)